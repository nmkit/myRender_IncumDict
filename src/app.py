import dash
from dash import dcc, html
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import datetime

w120_meaning_en_dict= np.load(r'../assets/w120_meaning_en_dict.npy', allow_pickle=True).item()
w120_meaning_zh_dict= np.load(r'../assets/w120_meaning_zh_dict.npy', allow_pickle=True).item()
sim_meaning_en_dict= np.load(r'../assets/sim_meaning_en_dict.npy', allow_pickle=True).item()
sim_meaning_zh_dict= np.load(r'../assets/sim_meaning_zh_dict.npy', allow_pickle=True).item()

simple_text = dcc.Markdown('{}'.format('a')
)
full_text = dcc.Markdown('{}'.format('b')
)


app = dash.Dash(__name__, use_pages=True,
                external_stylesheets=[dbc.themes.COSMO],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-XBHBEWB5RR"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
        
          gtag('config', 'G-XBHBEWB5RR');
        </script>
        
        
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        
    </body>
</html>
'''

server = app.server


app.layout = dbc.Container([

    dbc.Row(
        dbc.Col([html.H2("產權負擔字典Incumbrance Dictionary",
                        className='text-center text-primary'),
                html.Hr(),


                ], width=12),



    ),

    # content of each page
    dash.page_container,

    dbc.Col([html.Div("由樓訊易有限公司提供Provided by Proinfo Tech Limited",
                            className='text-center'),
                    html.Hr(),


                    ], width=12),



    ]
, fluid=True)

# Callback section: connecting the components
# ************************************************************************
# Line chart - Single
@app.callback(
    [Output(component_id='simple_text', component_property='children'), Output(component_id='collapse_en', component_property='children') ],
    Input('my-dpdn', 'value'),
    prevent_initial_call=True
)
def update_text(selected_incum):
    print(w120_meaning_en_dict[selected_incum])
    w120_list= w120_meaning_en_dict[selected_incum].split('\n')

    return "Explanation: "+ sim_meaning_en_dict[selected_incum] , html.Ul(id='my-list', children=[html.Li(i) for i in w120_list])

@app.callback(
    [Output(component_id='simple_text_zh', component_property='children'), Output(component_id='collapse_zh', component_property='children') ],
    Input('my_dpdn_zh', 'value'),
    prevent_initial_call=True
)
def update_text(selected_incum):
    print(w120_meaning_zh_dict[selected_incum])
    w120_list_zh= w120_meaning_zh_dict[selected_incum].split('\n')

    return "解釋: "+ sim_meaning_zh_dict[selected_incum] , html.Ul(id='my_list_zh', children=[html.Li(i) for i in w120_list_zh])


@app.callback(
    Output("collapse_en", "is_open"),
    [Input("button-question-1", "n_clicks")],
    [State("collapse_en", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse_zh", "is_open"),
    [Input("button-question-1", "n_clicks")],
    [State("collapse_zh", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True, port=8055)