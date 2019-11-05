# Import libraries
from scripts import pre_processing as prep
from scripts import exploration as exp
import pandas as pd
from glob import glob


# Import the data and read from CSV file
event_df = pd.read_csv('game_event_report.csv')


param_reports = glob('param_reports/*.csv')
param_df = pd.DataFrame()
for report in param_reports:
    new_df = pd.read_csv(report)
    param_df = param_df.append(new_df, ignore_index=True)



# event_df['event_key'] = event_df.entity_type.map(str) + '_' + event_df.event_type




# binarised_event_keys = prep.binarise(event_df.event_key)
#
# processed_event_df = pd.DataFrame()
# for event_key in binarised_event_keys.keys():
#     processed_event_df[event_key] = binarised_event_keys[event_key]
#
# concatenated_df = pd.concat([event_df, processed_event_df], axis=1, sort=False)
#
# concatenated_df.drop('id', 1)
# exp.correlation_matrix(concatenated_df, 'Correlation Matrix')
#
#
#
#
# test_event_df = event_df[(event_df.event_key == 'dude_harvested_resource_tree')]
# exp.histogram(test_event_df.time, 'Buildings Fixed Over Time', 30, (0, 300000))
#
# exp.time_animate_graph(exp.location_heatmap, test_event_df, 'pos_x', 'pos_y', 'Heatmap of Trees Harvested')


# # Display an event plot and bar chart for age
# exp.bar_chart(df['age.discretised'], 'Age Groups')



# exp.correlation_matrix(param_df, 'Summary Stat Correlation Matrix', exclude_features=['building_max_health'])



# exp.scatter_plot(param_df.time, param_df.dude_population, None,
#                  '2D Scatter', xlabel='x-coordinate', ylabel='y-coordinate')

param_dict = {}
for report_path in param_reports:
    param_dict[report_path] = pd.read_csv(report_path)

exp.line_graphs(param_dict, 'time', 'building_population',
                'Building Population Over Time', xlabel='time', ylabel='population')