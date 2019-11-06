# Import libraries
from scripts import pre_processing as prep
from scripts import exploration as exp
import pandas as pd
from glob import glob


# Import the data and read from CSV file and add event key feature
event_df_v1 = pd.read_csv('v1/game_event_report.csv')
event_df_v1['event_key'] = event_df_v1.entity_type.map(str) + '_' + event_df_v1.event_type
event_df_v2 = pd.read_csv('v2/game_event_report.csv')
event_df_v2['event_key'] = event_df_v1.entity_type.map(str) + '_' + event_df_v1.event_type

# Get a list of all param reports in the folders and sort them
param_reports_v1 = glob('v1/param_reports/*.csv')
param_reports_v1.sort()
param_reports_v1_2 = glob('v1_2/param_reports/*.csv')
param_reports_v2 = glob('v2/param_reports/*.csv')
param_reports_v2.sort()


# Create a list of all summary stats
summary_stats_dict = {'Dude': 'dude_population',
                      'Tree': 'tree_population',
                      'Food': 'food_population',
                      'Plant': 'plant_population',
                      'Building': 'building_population'}

# Create a list of all interesting events
events_dict = {'Trees Spawned': 'tree_spawned',
               'Trees Harvested': 'dude_harvested_resource_tree',
               'Buildings Fixed': 'dude_fixed_building',
               'Buildings Spawned': 'building_spawned'}

# exp.scatter_plot(param_df.time, param_df.dude_population, None,
#                  '2D Scatter', xlabel='x-coordinate', ylabel='y-coordinate')


def histogram_events(event_df):
    # Create visualisation for each feature
    for event, key in events_dict.items():
        exp.histogram(event_df[(event_df.event_key == key)].time,
                      event + ' Over Time', 30, (0, 300000))


def correlation_matrix_events(event_df):
    # Binarise the event keys
    binarised_event_keys = prep.binarise(event_df.event_key)
    # Add the event keys back into the data frame and concat them
    processed_event_df = pd.DataFrame()
    for event_key in binarised_event_keys.keys():
        processed_event_df[event_key] = binarised_event_keys[event_key]
    concatenated_df = pd.concat([event_df, processed_event_df], axis=1, sort=False)
    # Remove the id feature
    concatenated_df.drop('id', 1)
    # Create the visualisation
    exp.correlation_matrix(concatenated_df, 'Correlation Matrix')


def correlation_matrix_params(param_reports):
    # Import all param reports into one data frame
    param_df = pd.DataFrame()
    for report in param_reports:
        new_df = pd.read_csv(report)
        param_df = param_df.append(new_df, ignore_index=True)
    # Create the visualisation
    exp.correlation_matrix(param_df, 'Summary Stat Correlation Matrix')


def animated_heatmap_events(event_df):
    # Create visualisation for each feature
    for event, key in events_dict.items():
        exp.time_animate_graph(exp.location_heatmap, event_df[(event_df.event_key == key)],
                               'pos_x', 'pos_y', 'Heatmap of ' + event, key)


def line_graph_params(param_reports):
    # Import all summary stats to a dictionary
    param_dict = {}
    for report_path in param_reports:
        param_dict[report_path] = pd.read_csv(report_path)
    # Create visualisation for each feature
    for feature, key in summary_stats_dict.items():
        exp.line_graph(param_dict, 'time', key,
                       feature + ' Population Over Time',
                       xlabel='time', ylabel='population',
                       mask_paths=[
                           'v1/param_reports/game_param_report_',
                           'v1_2/param_reports/game_param_report_',
                           'v2/param_reports/game_param_report_'])


# Run features
# line_graph_params(param_reports_v2)
# correlation_matrix_params(param_reports_v1)
# animated_heatmap_events(event_df_v2)
# correlation_matrix_events(event_df_v1)
# histogram_events(event_df_v1)
