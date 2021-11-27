import textwrap

import pandas as pd

def wrap_text(str_series: pd.Series, width: int) -> pd.Series:
    """Take a series with string values, wrap
    them at a certain width for use in labels"""
    return str_series.transform(
        lambda x:
        '<br>'.join(textwrap.wrap(x, width=width))
    )