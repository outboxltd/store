# Connect to the database
import pymysql


def connect_2_db():
    connection = pymysql.connect(host="localhost",
                                 user="root",
                                 password="19371937",
                                 db="book_store",
                                 charset="utf8",
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

# :)
