# Import libraries
from scripts import pre_processing as prep
from scripts import exploration as exp
import pandas as pd


# Import the data and read from Excel file
df = pd.read_csv('gameplay_report.csv')

print(df)

# Perform discretisation for 'age'
discretised_age = prep.discretise_age(df['age'])

# Perform binarisation for 'marital'
binarised_marital = prep.binarise_marital(df['marital'])

# Perform binarisation for 'y'
binarised_y = prep.binarise_y_n(df['y'])

# Create a combined data frame of pre-processed data for analysis
processed_df = pd.DataFrame({
    'Married': binarised_marital['married'],
    'Y': binarised_y
})


# Combine the original data to the processed data for analysis
concatenated_df = pd.concat([df, processed_df], axis=1, sort=False)


# Display a correlation matrix for the entire data set
exp.correlation_matrix(concatenated_df, 'Banking Campaign - Correlation Matrix')

# Display an event plot and bar chart for age
exp.event_plot(df['age'], 'Age', orientation='vertical')
exp.bar_chart(df['age.discretised'], 'Age Groups')

# Display a histogram for duration
exp.histogram(df['duration'], 'Contact Durations', 30, (0, 2000))

# Display a scatter plot depicting age on duration
exp.scatter_plot(df['age'], df['duration'], df['y'],
                 'Contact Duration by Age', xlabel='Age', ylabel='Duration of Contact')
