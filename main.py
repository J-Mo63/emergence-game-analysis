# Import libraries
from scripts import pre_processing as prep
from scripts import exploration as exp
import pandas as pd
from glob import glob


# Import the data and read from CSV file and add event key feature
event_df = pd.read_csv('game_event_report.csv')
event_df['event_key'] = event_df.entity_type.map(str) + '_' + event_df.event_type

# Get a list of all param reports in the folder
param_reports = glob('param_reports/*.csv')

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


def histogram_events():
    # Create visualisation for each feature
    for event, key in events_dict.items():
        exp.histogram(event_df[(event_df.event_key == key)].time,
                      event + ' Over Time', 30, (0, 300000))


def correlation_matrix_events():
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


def correlation_matrix_params():
    # Import all param reports into one data frame
    param_df = pd.DataFrame()
    for report in param_reports:
        new_df = pd.read_csv(report)
        param_df = param_df.append(new_df, ignore_index=True)
    # Create the visualisation
    exp.correlation_matrix(param_df, 'Summary Stat Correlation Matrix')


def animated_heatmap_events():
    # Create visualisation for each feature
    for event, key in events_dict.items():
        exp.time_animate_graph(exp.location_heatmap, event_df[(event_df.event_key == key)],
                               'pos_x', 'pos_y', 'Heatmap of ' + event, key)


def line_graph_params():
    # Import all summary stats to a dictionary
    param_dict = {}
    for report_path in param_reports:
        param_dict[report_path] = pd.read_csv(report_path)
    # Create visualisation for each feature
    for feature, key in summary_stats_dict.items():
        exp.line_graph(param_dict, 'time', key, feature + ' Population Over Time',
                       xlabel='time', ylabel='population')

# Run features
# line_graph_params()
# correlation_matrix_params()
# animated_heatmap_events()
# correlation_matrix_events()
# histogram_events()
