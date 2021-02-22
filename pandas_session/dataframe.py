"""ref:https://note.nkmk.me/python-pandas-dataframe-values-columns-index/"""
import pandas as pd
import numpy as np


def get_tmp_df():
    return pd.DataFrame(np.arange(12).reshape(3, 4),
                        columns=['col_0', 'col_1', 'col_2', 'col_3'],
                        index=['row_0', 'row_1', 'row_2'])
