# Goodreads Ratings
A simple Dash app for visualizing Goodreads data.

## Data sources
This project pulls from two primary data sources.

The first is the ["Goodreads-books" dataset](https://www.kaggle.com/jealousleopard/goodreadsbooks) from Kaggle.

The second is a scraped dataset that uses the Kaggle data's ISBN codes to export metadata and categories from the Google Books services. We use [isbnlib](https://pypi.org/project/isbnlib/) to peform the data scraping.