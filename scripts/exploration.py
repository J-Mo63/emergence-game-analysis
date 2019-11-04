# Import libraries
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import imageio


def time_animate_graph(graph, df, x_col, y_col, title):
    matplotlib.use('Agg')
    imageio.mimsave('../output/animated_graph.gif',
                    [graph(df, i*10000, x_col, y_col, title) for i in range(31)],
                    fps=10)
    matplotlib.use('module://backend_interagg')


def location_heatmap(df, i, x_col, y_col, title):
    curr_df = df[(df.time <= i)]
    plt.hist2d(curr_df[x_col].values, curr_df[y_col].values, bins=[30, 20], range=[[-500, 1500], [-500, 1000]])
    plt.gca().invert_yaxis()
    fig = plt.gcf()
    time = "{:02.2f}".format(i/60000).replace(".", ":")
    plt.title(title + ' (' + time + ' minutes)')

    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    return image


def correlation_matrix(df, title, **kwargs):
    if kwargs.get('exclude_features'):
        for feature in kwargs.get('exclude_features'):
            df.drop(feature, axis=1, inplace=True)

    # Set up the matrix plot and display
    f, ax = plt.subplots(figsize=(20, 16))
    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(corr, mask=mask,
                cmap=sns.diverging_palette(220, 10, as_cmap=True),
                square=True, ax=ax).set_title(title)
    plt.show()


def bar_chart(df, title, **kwargs):
    # Get the values and counts from the data frame
    value_counts = df.value_counts()

    # Check for custom sorting dictionary in kwargs
    if kwargs.get('sorting_criteria'):
        # Get the kwarg value for the sorting criteria
        sorting_criteria = kwargs.get('sorting_criteria')

        # Create lists of the pre-allocated size
        sizes = [None] * len(sorting_criteria)
        labels = [None] * len(sorting_criteria)
        for i in range(len(value_counts)):
            # Populate the lists by the sorting values
            sorting_value = sorting_criteria[value_counts.index[i]]
            labels[sorting_value] = value_counts.index[i].replace('.', ' ').title()
            sizes[sorting_value] = value_counts[i]
        # Remove null items from the list
        sizes = list(filter(None, sizes))
        labels = list(filter(None, labels))
    else:
        # Separate the labels from the counts and create the lists
        sizes = []
        labels = []
        for i in range(len(value_counts)):
            labels.append(value_counts.index[i]
                          .replace('.', ' ').title() + ' (' + str(value_counts[i]) + ')')
            sizes.append(value_counts[i])

    # Check for slicing options in the kwargs
    labels = labels[kwargs.get('l_slice'):kwargs.get('r_slice')]
    sizes = sizes[kwargs.get('l_slice'):kwargs.get('r_slice')]

    # Apply the labels and sizes to the graph portions and display
    plt.bar(labels, sizes, align='center', alpha=1)
    plt.xticks(labels)
    plt.ylabel(kwargs.get('ylabel') if kwargs.get('ylabel') else 'Amount')
    plt.title(title)
    plt.show()


def scatter_plot(df_x, df_y, df_z, title, **kwargs):
    # Colour the points gold if there is a third value
    if df_z:
        colouring = ['gold' if value == 'yes' else 'C0' for value in df_z.values]
        plt.scatter(df_x, df_y, c=colouring)
    else:
        plt.scatter(df_x, df_y)
    plt.title(title)
    plt.xlabel(kwargs.get('xlabel') if kwargs.get('xlabel') else 'x value')
    plt.ylabel(kwargs.get('ylabel') if kwargs.get('ylabel') else 'y value')
    plt.show()


def histogram(df, title, bins, display_range, **kwargs):
    plt.hist(df, bins=bins, range=display_range)
    plt.ylabel(kwargs.get('ylabel') if kwargs.get('ylabel') else 'Amount')
    plt.title(title)
    plt.show()
