#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 Hengda Shi <hengda.shi@engineering.ucla.edu>
#
# Distributed under terms of the MIT license.

"""

"""

import plotly.graph_objects as go

from ml.utils.statistics.common import compute_stats

def plot_dist(df):
    stats_df = df.apply(compute_stats).T
    fig = go.Figure()

    fig.add_trace(go.Box(
        q1=stats_df._q1,
        median=stats_df._median,
        q3=stats_df._q3,
        lowerfence=stats_df._lower,
        upperfence=stats_df._upper,
        mean=stats_df._mean,
        sd=stats_df._std
    ))

    fig.show()
