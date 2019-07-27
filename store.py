from bottle import route, run, template, static_file, get, post, delete, request, response
from sys import argv
import json
import pymysql
import db

connection = db.connect_2_db()


@get("/admin")
def admin_portal():
    return template("pages/admin.html")


@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')

# show all books
@get("/allbooks")
def get_books():
    with connection.cursor() as cursor:
        sql = "select * from books"
        cursor.execute(sql)
        return json.dumps(cursor.fetchall())

# get only 1 book
@get("/book/<id>")
def get_student(id):
    with connection.cursor() as cursor:
        sql = f"select * from books where ID = '{id}'"
        cursor.execute(sql)
        return json.dumps(cursor.fetchone())

# @post("/addbook")
# def add():
#     book_id = request.json.get("id")
#     title = request.json.get( "title")
#     author = request.json.get("author")
#     book_description = request.json.get("book_description")
#     favorite = request.json.get("Favorite")
#     price = request.json.get("price")
#     img_url = request.json.get("img_url")
#     categoryid = request.json.get("categoryid")
#     print("hiiii" + book_id)
#     try:
#         with connection.cursor() as cursor:
#             sql = f"insert into books values ('{book_id}','{title}','{author}','{book_description}','{favorite}','{price}','{img_url}','{categoryid}')"
#             cursor.execute(sql)
#             connection.commit()
#             response.status = 201
#         return 'book Added!'
#     except:
#         return 'book Not Added...'


@route('/addbook', method="POST")
def add():
    add_item = {"id": request.json.get("id")}
    print(add_item)
    return "done"


@get("/draft")
def draft():
    return template("draft.html")


run(host="localhost", port=4700, debug=True, reloder=True)
# run(host='0.0.0.0', port=argv[1])
