from django.apps import AppConfig

import pandas as pd


class PandasConf(AppConfig):
    # displays all columns in data frames.
    pd.set_option('expand_frame_repr', False)
    # Max rows displayed.
    pd.set_option('display.max_rows', 10)
