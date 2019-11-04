# Import libraries
from scripts import pre_processing as prep
from scripts import exploration as exp
import pandas as pd


# Import the data and read from Excel file
df = pd.read_csv('gameplay_report.csv')


df['event_key'] = df.entity_type.map(str) + '_' + df.event_type


binarised_event_keys = prep.binarise(df.event_key)

processed_df = pd.DataFrame()
for event_key in binarised_event_keys.keys():
    processed_df[event_key] = binarised_event_keys[event_key]

concatenated_df = pd.concat([df, processed_df], axis=1, sort=False)



exp.correlation_matrix(concatenated_df, 'Correlation Matrix')

test_df = df[(df.event_key == 'dude_fixed_building')]


exp.histogram(test_df.time, 'Buildings Fixed Over Time', 30, (0, 300000))

exp.time_animate_graph(exp.location_heatmap, test_df, 'pos_x', 'pos_y', 'Heatmap')





# # Display an event plot and bar chart for age
# exp.event_plot(df['age'], 'Age', orientation='vertical')
# exp.bar_chart(df['age.discretised'], 'Age Groups')


# Display a scatter plot depicting age on duration
# exp.scatter_plot(test_df['pos_x'], test_df['pos_y'], None,
#                  'Dude Building Creation', xlabel='x-coordinate', ylabel='y-coordinate')
