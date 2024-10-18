from flask import Flask
from flask import jsonify
import MySQLdb

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Welcome to the multi-container Flask app!")

@app.route('/db')
def db_test():
    db = MySQLdb.connect(host="db", user="root", passwd="root", db="test_db")
    cursor = db.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    db.close()
    return jsonify(tables=tables)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
