# health_reports module
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
import matplotlib.dates as mdates

pd.options.mode.copy_on_write = True

def date_mmddyyyy(date_str, sep='/'):
    month, day, year = date_str.split(sep)
    return date(int(year), int(month), int(day))

def date_yyyymmdd(date_str, sep='-'):
    year, month, day = date_str.split(sep)
    return date(int(year), int(month), int(day))
    
def high_or_low(value, min_value, max_value):
    if value > max_value:
        return 1
    elif value < min_value:
        return -1
    else:
        return 0

def bloodwork_report(cat, savefig=False):
    cat_min = blood_dict.loc[cat, 'min']
    cat_max = blood_dict.loc[cat, 'max']
    cat_name = cat
    cat_type = blood_dict.loc[cat, 'dtype']

    data = bloods[['date', cat]]
    
    if cat_type in [float, 'float']:
        data['extrema'] = data[cat].apply(lambda x: high_or_low(x, cat_min, cat_max))
        
        fig, ax = plt.subplots()

        if (data[cat].max() > cat_max > 0) or (data[cat].min() < cat_min and cat_min >= 0):
            sns.scatterplot(data=data, x='date', y=cat, hue='extrema')

            ax.axhline(cat_min, xmin=0, xmax=1, c='gray')
            ax.axhline(cat_max, xmin=0, xmax=1, c='gray')
            
            h, l = ax.get_legend_handles_labels()
            ax.legend(h, l)
            
            leg_map = {'0': 'Normal', '1': 'High', '-1': 'Low'}
            handles, labels = ax.get_legend_handles_labels()
            ax.legend(handles, [leg_map[l] for l in labels])

        else:
            sns.scatterplot(data=data, x='date', y=cat)
            if cat_max > 0:
                ax.axhline(cat_min, xmin=0, xmax=1, c='gray')
            if cat_min >= 0:
                ax.axhline(cat_max, xmin=0, xmax=1, c='gray')
        
        ax.xaxis.set_major_formatter(
            mdates.ConciseDateFormatter(ax.xaxis.get_major_locator())
        );
        ax.set_xlabel('Date')
        ax.set_ylabel(cat_name)
        ax.set_title(f"Mel's {cat_name}");

        if savefig==True:
            plt.savefig(f"images/{cat}.jpg")
        
        plt.show(fig)
        plt.close(fig)

        return None

    elif cat_type == str:
        pass