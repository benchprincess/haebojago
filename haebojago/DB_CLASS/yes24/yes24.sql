USE yes24;

-- CREATE TABLE Books(
-- bookID INT AUTO_INCREMENT PRIMARY KEY,
-- title VARCHAR(255) NOT NULL,
-- author VARCHAR(255),
-- publisher VARCHAR(255),
-- publishing DATE,
-- rating DECIMAL(3, 1),
-- review INT,
-- sales INT,
-- price DECIMAL(10, 2),
-- ranking INT,
-- ranking_weeks INT
-- );

-- SELECT title, author FROM books;
-- SELECT * FROM books WHERE rating >= 4.0;
-- SELECT title, review FROM books WHERE review >= 100 ORDER BY review DESC;
-- SELECT title, price FROM books WHERE price < 20000;
-- SELECT * FROM books WHERE ranking_weeks >=4 ORDER BY ranking_weeks DESC; 
-- SELECT * FROM books WHERE author = '자청 저';
-- SELECT * FROM books WHERE pulisher = '웅진지식하우스' 

-- SELECT author, COUNT(*) AS books_count FROM books GROUP BY author ORDER BY books_count DESC;
-- SELECT publisher, COUNT(*) AS publishing_count FROM books GROUP BY publisher
-- ORDER BY publishing_count DESC LIMIT 1;
-- SELECT author, AVG(rating) AS rating_avg FROM books GROUP BY author ORDER BY rating_avg
-- SELECT * FROM books WHERE ranking = 1; 
-- SELECT title, sales, review FROM books ORDER BY sales DESC, review DESC LIMIT 10;
-- SELECT * FROM books ORDER BY publising DESC LIMIT 5;

-- SELECT author, AVG(rating) FROM books GROUP BY author ORDER BY rating_avg;
-- SELECT publishing, COUNT(*) FROM books GROUP BY publishing;
-- SELECT title, AVG(price) FROM books GROUP BY title;
-- SELECT * FROM books ORDER BY review DESC LIMIT 5;
-- SELECT ranking, AVG(review) FROM books GROUP BY ranking;

-- SELECT title, rating FROM books WHERE rating > (SELECT AVG(rating))
-- ORDER BY rating DESC;
-- SELECT title, price FROM books WHERE price > (SELECT AVG(price) FROM books);
-- SELECT title, review FROM books WHERE review > (SELECT MAX(review) FROM books);
-- SELECT author, title FROM books WHERE author = (
-- SELECT author, COUNT(*) FROM books GROUP BY author ORDER BY COUNT(*) DESC);

-- UPDATE Books SET price = 99999 WHERE title = "한국사";
-- UPDATE Books SET title = '제목 업데이트' WHERE author = '최태성 저';
-- DELETE FROM books WHERE sales = (SELECT MIN(sales) FROM books);
-- UPDATE books SET rating = rating+1 WHERE publisher = '웅진하우스';

-- SELECT author, AVG(rating), AVG(sales) FROM books GROUP BY author ORDER BY AVG(rating) DESC, AVG(sales) DESC;
-- SELECT publishing FROM books GROUP BY publishing ORDER BY publishing_date ASC;
-- SELECT publisher, COUNT(*) AS book_count, SUM(review) AS review_sum FROM books GROUP BY publisher ORDER BY book_count DESC;
-- SELECT ranking, AVG(sales) FROM books GROUP BY ranking;
-- SELECT price, AVG(review), AVG(rating) FROM books GROUP BY price;

