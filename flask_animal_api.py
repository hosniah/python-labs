import json
from flask import Flask, Response, abort
from .utils import JSON_MIME_TYPE, search_book
import pymysql

app = Flask(__name__)

db = pymysql.connect("localhost", "root", "", "m2i_python_db")

@app.route('/animals')
def book_list():
    cursor = db.cursor()
    sql = "SELECT * FROM animal"
    cursor.execute(sql)
    results = cursor.fetchall()
    response = Response(
        json.dumps(results), status=200, mimetype=JSON_MIME_TYPE)
    return response

@app.errorhandler(404)
def not_found(e):
    return '', 404
