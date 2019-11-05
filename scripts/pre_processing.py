# Import libraries
from sklearn import preprocessing


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
