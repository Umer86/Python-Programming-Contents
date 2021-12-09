colorscale = [[0, '#edf8fb'], [.3, '#00BFFF'], [.6, '#8856a7'], [1, '#810f7c']]

heatmap = go.Heatmap(z=heat.values, x=heat.columns, y=heat.index, colorscale=colorscale)
data2 = [heatmap]
layout = go.Layout(

    title='Top 40 Worst Terror Attacks in History from 1982 to 2016',
    xaxis=dict(ticks='', nticks=20),
    yaxis=dict(ticks='')

)
fig = go.Figure(data=data2, layout=layout)
py.iplot(fig, filename='heatmap', show_link=False)
