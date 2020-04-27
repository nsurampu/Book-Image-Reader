import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from pathlib import Path
import pickle

# rotor_app = dash.Dash(__name__)
from app import app

app.title = 'Book Image Reader'

init_run = True

if Path('page_cache.pickle').is_file():
    current_page = 0
    with open('page_cache.pickle', 'rb') as handle:
        all_pages = pickle.load(handle)
        page_options = []
        for key in all_pages:
            page_options.append({'label': 'Page ' + key, 'value': key})

else:
    current_page = 0
    all_pages = {}
    page_options = [{'label': 'No Pages Available', 'value': '-1'}]

app.layout = html.Div(style={'width':"100%"}, children=[

    dcc.Markdown(children="# Book Image Reader: A Web App for Reading Books in Picture Formats (jpeg, png etc.)"),

    # dcc.Markdown(id="status", children="#### Status: No Images Loaded"),
    dcc.ConfirmDialog(
        id='confirm',
        message='Page Loading into App Completed!!!'
    ),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            html.A('Click Here to Select File')
        ]),
        style={
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),

    html.Div(children=[
        html.Button('Continue to NEXT PAGE --->', id='next_page')
    ]),

    html.Div(children=[
        dcc.Markdown("##### You are currently on this page: (To jump to a page scroll down and choose from menu)")
    ]),

    html.Div(children=[
        html.Img(id='next_page_image')
    ]),

    dcc.Markdown("#### To jump to a page, choose from menu, check page preview below and scroll back up to continue reading by clicking on the next page button"),

    html.Div(children=[
        dcc.Dropdown(
            id='page_drop',
            options=page_options,
            value='0',
            placeholder='Jump to Page...'
        )
    ]),

    html.Div(children=[
        dcc.Markdown("##### You jumped to this page. Go back up to continue reading from the next page:")
    ]),

    html.Div(children=[
        html.Img(id='prev_page_image')
    ])
])

@app.callback([Output('confirm', 'displayed'),
                Output('page_drop', 'options')],
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
              State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    global current_page
    global all_pages
    global page_options
    global init_run

    if Path('page_cache.pickle').is_file() and init_run:
        current_page = 0
        with open('page_cache.pickle', 'rb') as handle:
            all_pages = pickle.load(handle)
            page_options = []
            for key in all_pages:
                page_options.append({'label': 'Page ' + key, 'value': key})
            init_run = False

            return True, page_options

    all_pages = {}
    current_page = 0
    page_options = []
    if isinstance(list_of_contents, list):
        for i in range(len(list_of_contents)):
            all_pages[list_of_names[i].split(".")[0]] = list_of_contents[i]

        sorted_pages = {}
        for key in sorted(all_pages.keys()):
            sorted_pages[key] = all_pages[key]

        all_pages = sorted_pages
        for key in all_pages:
            page_options.append({'label': 'Page ' + key, 'value': key})

        with open('page_cache.pickle', 'wb') as handle:
            pickle.dump(all_pages, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return True, page_options

@app.callback(
Output(component_id='prev_page_image',component_property='src'),
[Input(component_id='page_drop', component_property='value')]
)
def show_prev(page_no):
    global current_page
    global all_pages
    if isinstance(page_no, str):
        if int(page_no)>0:
            current_page = int(page_no)-1
        else:
            current_page = 0
        return list(all_pages.values())[current_page]

@app.callback(
Output(component_id='next_page_image',component_property='src'),
[Input(component_id='next_page', component_property='n_clicks')]
)
def show_next(clicks):
    global current_page
    global all_pages
    if isinstance(current_page, int):
        if current_page+1<len(all_pages):
            current_page += 1
            return list(all_pages.values())[current_page]
        else:
            return list(all_pages.values())[current_page]


if __name__=="__main__":
    app.run_server(debug=False)
