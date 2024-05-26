

app.layout = [ html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Map(figure=)
]


if __name__ == '__main__':
    app.run(debug=True)