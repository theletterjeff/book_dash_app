# Native
import os
import sqlite3 as sql
import textwrap

# Third party
from codetiming import Timer
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

# Dash
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Custom
from lib import graph_helper
import lib.database_helper as db

t = Timer()

app = dash.Dash(__name__)
server = app.server

db_path = os.path.abspath('data/books.db')
with db.connect(db_path) as con:
    sql = """
        SELECT ta.isbn13, ta.author, ta.title, c.cat_descrip, bk.ratings_count, bk.average_rating
        FROM titles__authors ta, titles__cat_codes tcc, books_kaggle bk, categories c 
        WHERE ta.isbn13 = tcc.isbn13
            AND ta.isbn13 = bk.isbn13
            AND c.cat_code = tcc.cat_code 
            and bk.ratings_count > 100
        ORDER BY bk.average_rating DESC;
    """
    df = pd.read_sql(sql, con)

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
        # Text
        dcc.Markdown('''Choose one or more authors:'''),

        # Dropdown filter
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': label, 'value': label}
                for label
                in df['author'].sort_values().unique()
            ],
            value=['Alice Munro'],
            multi=True,
    )], style={'width': '30%'}),

    html.Br(),

    # Graph
    html.Div([
        dcc.Graph(id='graph'),
    ], style={'width': '75%'}
    ),

    html.Div([
        dcc.Markdown("""
            This project pulls from two primary data sources. The first is the ["Goodreads-books" dataset](https://www.kaggle.com/jealousleopard/goodreadsbooks) from Kaggle. The second is a scraped dataset that uses the Kaggle data's ISBN codes to export metadata and categories from the Google Books service. We use [isbnlib](https://pypi.org/project/isbnlib/) to peform the data scraping.
        """)
    ], style={
        'width': '50%',
        'fontSize': '12px',
    })

], style={
    'position': 'relative',
    'left': '10px',
})


@app.callback(
    Output('graph', 'figure'),
    Input('dropdown', 'value')
)
def update_graph(authors: list):
    fig = go.Figure()

    if len(authors) > 0:
        filtered_df = df.loc[df.author.isin(authors)]
        filtered_df = filtered_df.sort_values(by='average_rating')
        filtered_df = filtered_df.drop_duplicates(subset=['title'])
        filtered_df = filtered_df.drop_duplicates(subset=['isbn13'])

        # Wrap titles
        filtered_df['title'] = graph_helper.wrap_text(filtered_df['title'], 40)

        # Set author colors
        authors_unique = filtered_df['author'].unique()
        authors_num = len(authors_unique)
        author_colors = px.colors.qualitative.Plotly[:authors_num]

        for idx, author in enumerate(authors_unique):
            author_df = filtered_df.copy()
            author_df.loc[filtered_df['author'] != author, 'average_rating'] = np.nan
        
            fig.add_trace(go.Bar(
                x=author_df['average_rating'],
                y=author_df['title'],
                orientation='h',
                marker_color=author_colors[idx],
                text=author_df['average_rating'],
                name=author,
            ))

        # Set some core graph attributes
        fig.update_layout(
            height= 170 + len(filtered_df) * 50,
            title='Books with Goodreads Ratings',
            barmode='relative',
            font=dict(size=14),
        )

        # Set legend
        fig.update_layout(
            showlegend=True,
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1,
                xanchor='right',
                x=1,
            )
        )

    return fig

if __name__ == '__main__':
    app.run_server(debug=False)
