import pandas as pd


def config_pandas():
    # displays all columns in data frames.
    pd.set_option('expand_frame_repr', False)
    # Max rows displayed.
    pd.set_option('display.max_rows', 10)


if __name__  == "__main__":
    config_pandas()
