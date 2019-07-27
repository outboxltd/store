-- create database book_store;
-- use book_store;

-- CREATE TABLE categories (
--     ID int NOT NULL,
--     title varchar(255) NOT NULL,
--     PRIMARY KEY (ID)
-- );

-- CREATE TABLE books (
--     ID int NOT NULL,
--     title varchar(255) NOT NULL,
--     author varchar(255),
--     book_description varchar(1000),
--     Favorite bool,
--     price float,
--     img_url varchar(255),
--     categoryId int,
--     PRIMARY KEY (ID),
-- 	FOREIGN KEY (categoryId) REFERENCES categories(ID)
-- )

 -- insert into categories(ID,title) value (2,"fun")

 -- INSERT INTO `book_store`.`books` (`ID`, `title`, `author`, `book_description`, `Favorite`, `price`, `img_url`, `categoryId`) VALUES ('2', 'how to fart in front of your boyfriend', 'steve wonder', 'A method that works for years without acknowledging unpleasant smells', '1', '99', 'https://www.standardmedia.co.ke/evemedia/eveimages/tuesday/thumb_jklofohqvovgfq8oh5a82da4493339.jpg', '1');

-- ### join book title to category title 
-- SELECT books.title,books.author, categories.title
-- FROM books
-- INNER JOIN categories ON books.categoryId = categories.ID; 


