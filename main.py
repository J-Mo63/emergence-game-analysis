# Import libraries
from scripts import pre_processing as prep
from scripts import exploration as exp
import pandas as pd


# Import the data and read from CSV file
event_df = pd.read_csv('game_event_report.csv')
param_df = pd.read_csv('game_param_report.csv')


event_df['event_key'] = event_df.entity_type.map(str) + '_' + event_df.event_type


# binarised_event_keys = prep.binarise(event_df.event_key)
#
# processed_event_df = pd.DataFrame()
# for event_key in binarised_event_keys.keys():
#     processed_event_df[event_key] = binarised_event_keys[event_key]
#
# concatenated_df = pd.concat([event_df, processed_event_df], axis=1, sort=False)

# concatenated_df.drop('id', 1)
# exp.correlation_matrix(concatenated_df, 'Correlation Matrix')

exp.correlation_matrix(param_df, 'Correlation Matrix')

# test_event_df = event_df[(event_df.event_key == 'dude_harvested_resource_tree')]


# exp.histogram(test_df.time, 'Buildings Fixed Over Time', 30, (0, 300000))

# exp.time_animate_graph(exp.location_heatmap, test_event_df, 'pos_x', 'pos_y', 'Heatmap of Trees Harvested')


# # Display an event plot and bar chart for age
# exp.event_plot(df['age'], 'Age', orientation='vertical')
# exp.bar_chart(df['age.discretised'], 'Age Groups')


# Display a scatter plot depicting age on duration
# exp.scatter_plot(test_df['pos_x'], test_df['pos_y'], None,
#                  'Dude Building Creation', xlabel='x-coordinate', ylabel='y-coordinate')
