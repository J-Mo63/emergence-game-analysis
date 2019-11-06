# Import libraries
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import imageio
from scipy.signal import savgol_filter
from scipy.interpolate import interp1d


def time_animate_graph(graph, df, x_col, y_col, title, filename):
    matplotlib.use('Agg')
    imageio.mimsave('../output/' + filename + '.gif',
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


def line_graph(dfs, x_col, y_col, title, **kwargs):
    df_keys = list(dfs.keys())
    for i in range(len(df_keys)):
        df_key = df_keys[i]
        df = dfs[df_key]

        xx = np.linspace(df[x_col].min(), df[x_col].max(), 1000)

        # interpolate + smooth
        itp = interp1d(df[x_col], df[y_col], kind='linear')
        yy = savgol_filter(itp(xx), 101, 3)
        # Hide the full file path
        label = df_key
        if kwargs.get('mask_paths'):
            for path in kwargs.get('mask_paths'):
                label = label.replace(path, '').replace('.csv', '')
        style = '--' if i >= 10 else '-'
        plt.plot(xx, yy, style, label=label)

    plt.title(title)
    plt.xlabel(kwargs.get('xlabel') if kwargs.get('xlabel') else 'x value')
    plt.ylabel(kwargs.get('ylabel') if kwargs.get('ylabel') else 'y value')
    plt.legend()
    plt.show()
