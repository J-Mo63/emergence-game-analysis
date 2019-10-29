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


def binarise_y_n(df):
    # Isolate the values from the data frame
    df = df.values

    # Format the binarised items into one boolean column
    binarised_y_n_list = []
    for i in range(len(df)):
        item = df[i]
        if item == 'yes':
            binarised_y_n_list.append(1)
        else:
            binarised_y_n_list.append(0)

    # Return the results as a list
    return binarised_y_n_list


def binarise_marital(df):
    # Isolate the values from the data frame
    df = df.values

    # Binarise the categories
    binarised = preprocessing.LabelBinarizer().fit_transform(df)

    # Format the binarised items into three columns
    binarised_married_list = []
    binarised_single_list = []
    binarised_divorced_list = []
    for i in range(len(binarised)):
        item = binarised[i]
        binarised_divorced_list.append(item[0])
        binarised_married_list.append(item[1])
        binarised_single_list.append(item[2])

    # Return the results as a dictionary
    return {'married': binarised_married_list,
            'single': binarised_single_list,
            'divorced': binarised_divorced_list}
