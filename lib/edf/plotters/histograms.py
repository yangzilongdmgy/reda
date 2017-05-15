# import matplotlib as mpl
import pandas as pd
import pylab as plt
import matplotlib as mpl
mpl.rcParams['font.size'] = 8.0
import numpy as np
import edf.main.units as units


def plot_histograms(ertobj, keys, **kwargs):
    """Generate histograms for one or more keys in the given container

    Parameters
    ----------
    merge: bool
        if True, then generate only one figure with all key-plots as columns

    """
    # you can either provide a DataFrame or an ERT object
    if isinstance(ertobj, pd.DataFrame):
        df = ertobj
    else:
        df = ertobj.df

    figures = {}
    merge_figs = kwargs.get('merge', False)
    if merge_figs:
        nr_x = 2
        nr_y = len(keys)
        size_x = 10 / 2.54
        size_y = 5 * nr_y / 2.54
        fig, axes_all = plt.subplots(nr_y, nr_x, figsize=(size_x, size_y))
        axes_all = np.atleast_2d(axes_all)

    for row_nr, key in enumerate(keys):
        print('generating histogram plot for key: {0}'.format(key))
        subdata_raw = df[key].values
        subdata = subdata_raw[~np.isnan(subdata_raw)]
        subdata_log10_with_nan = np.log10(subdata)
        subdata_log10 = subdata_log10_with_nan[~np.isnan(
            subdata_log10_with_nan)
        ]

        if merge_figs:
            axes = axes_all[row_nr].squeeze()
        else:
            fig, axes = plt.subplots(1, 2, figsize=(10 / 2.54, 5 / 2.54))

        ax = axes[0]
        ax.hist(
            subdata,
            100,
        )
        ax.set_xlabel(
            units.get_label(key)
        )
        ax.set_ylabel('count')
        ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(5))

        if subdata_log10.size > 0:
            ax = axes[1]
            ax.hist(
                subdata_log10,
                100,
            )
            ax.set_xlabel(r'$log_{10}($' + units.get_label(key) + ')')
            ax.set_ylabel('count')
            ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(5))
        else:
            pass
            # del(axes[1])

        fig.tight_layout()

        if not merge_figs:
            figures[key] = fig

    if merge_figs:
        figures['all'] = fig
    return figures
