# Native
import os
import sqlite3 as sql

# Third party
from codetiming import Timer
import pandas as pd
from sqlalchemy import create_engine

# Dash
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

# Custom
import lib.database_helper as db

t = Timer()

app = dash.Dash(__name__)
server = app.server

db_path = os.path.abspath('data/books.db')
with db.connect(db_path) as con:
    df = pd.read_sql('SELECT * FROM books_kaggle', con)

app.layout = html.Div(className='base-page', children=[

    # Header
    html.Div(
        className='app-header',
        children=[
            html.H1('Book Lookup'),
            html.H2('A searchable database of books')
    ]),

    # Main
    html.Div([
        'placeholder'
    ])

])

if __name__ == '__main__':
    app.run_server(debug=True)