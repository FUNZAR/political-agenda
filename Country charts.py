import json
import plotly.graph_objs as go

import pandas as pd

with open() as f:
    data = json.load(f)

dates = sorted(list(data.keys()))
print(dates)
issues = sorted(list(set([issue for date in data for issue in data[date]])))

traces = []
for issue in issues:
    x = []
    y = []
    for date in dates:
        if issue in data[date]:
            x.append(date)
            y.append(data[date][issue])
    trace = go.Scatter(x=x, y=y, mode='lines', name=issue)
    traces.append(trace)

layout = go.Layout(title='Countries over time (Senators)')
fig = go.Figure(data=traces, layout=layout)
fig.update_xaxes(categoryorder='array', categoryarray=dates)
fig.update_traces(selector=lambda tmp: True, visible="legendonly")
fig.show()
