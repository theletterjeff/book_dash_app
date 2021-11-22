CREATE TABLE books_kaggle (
	book_id int,
	title varchar(300),
	authors varchar(200),
	average_rating float,
	isbn varchar(10),
	isbn13 int,
	language_code varchar(5),
	num_pages int,
	ratings_count int,
	text_reviews_count int,
	publication_date varchar(30),
	publisher varchar(200)
);

CREATE TABLE books_oclc (
	owi int,
	isbn13 int,
	title varchar(300),
	authors varchar(200),
	publisher varchar(200),
	publication_year varchar(30),
	language_code varchar(5),
	oclc int,
	lcc varchar(20),
	ddf varchar(20),
	categories varchar(1000)
);