#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 Hengda Shi <hengda.shi@engineering.ucla.edu>
#
# Distributed under terms of the MIT license.

"""

"""

import pandas as pd

def compute_stats(series):
    _q1 = series.quantile(q=0.25)
    _q2 = series.quantile(q=0.5)
    _q3 = series.quantile(q=0.75)
    _iqr = _q3 - _q1
    _upper = _q3 + 1.5 * _iqr
    _lower = _q1 - 1.5 * _iqr
    _max = series.max()
    _min = series.min()
    _mean = series.mean()
    _std = series.std()
    return pd.Series({
        '_q1': _q1,
        '_median': _q2,
        '_q3': _q3,
        '_upper': _upper,
        '_lower': _lower,
        '_max': _max,
        '_min': _min,
        '_mean': _mean,
        '_std': _std
    })
