from dash import Dash, html, dcc, dash_table
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#app = Dash(__name__)
df = pd.read_csv('/Users/renatabordovska/Desktop/all_data_dash.csv')

#dfagg 
fig = px.bar(df, x="client_id", y="loan", color="poutcome", barmode='group')

image_path1 = 'assets/Potatoes.png'



tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dcc.Graph(figure=px.histogram(df, x='poutcome', y='age', histfunc='avg')),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dcc.Graph(
        id='example-graph',
        figure=fig
    ),
        ]
    ),
    className="mt-3",
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Tab 1"),
        dbc.Tab(tab2_content, label="Tab 2")
    ]
)





app.layout = html.Div(children=[
    html.Div(
        [html.Img(src=image_path1, style={"width": "50px", "height": "50px", 'display': 'inline-block'}),
        html.H1(children='Algorithm potatoes: Second round of investments campaign', style={'display': 'inline-block'}),],
        style={'display': 'inline-block'}
        ),
    html.Br(),
    html.Br(),
    html.H2("Data"),
    html.Div(children='''
        Clients database:
    '''),
    #dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dbc.Table.from_dataframe(df.sample(10), striped=True, bordered=True, hover=True, responsive=True),
    #dbc.Table.from_dataframe(put df here, striped=True, bordered=True, hover=True, responsive = 'sm'),
    html.H2("Visualizations"),
    tabs,
    html.H2("Modelling"),
    html.H2("Campaign results"),
], style={"margin": "30px"})
if __name__ == '__main__':
    app.run(debug=True, port = 8080)
















