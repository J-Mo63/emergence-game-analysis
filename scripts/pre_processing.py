# Import libraries
from sklearn import preprocessing


def discretise_age(df):
    # Isolate the values from the data frame
    df = df.values

    # Discretise the age into categories
    discretised_list = []
    for i in range(df.size):
        item = df[i]
        if item < 45:
            discretised_list.append('Adult')
        elif item <= 65:
            discretised_list.append('Mid-age')
        elif item > 65:
            discretised_list.append('Old-age')
        else:
            discretised_list.append('NaN')

    # Return the results as a list
    return discretised_list


def binarise(df):
    # Binarise the categories
    binarised = preprocessing.LabelBinarizer().fit_transform(df.values)
    # Get the labels and sort them
    labels = df.unique().tolist()
    labels.sort()
    # Append the binarised values to a dictionary
    binarised_dict = {}
    for item in binarised:
        for i in range(len(labels)):
            label = labels[i]
            if label not in binarised_dict:
                binarised_dict[label] = []
            binarised_dict[label].append(item[i])
    # Return the dictionary
    return binarised_dict
