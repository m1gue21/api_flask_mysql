from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

connection = MySQL(app)


def page_not_found(error):
    return "<h1>Page not found, verify the URL</h1>"


@app.route('/courses', methods=['GET'])
def list_courses():
    try:
        cursor = connection.connection.cursor()
        sql = "SELECT * FROM course"
        cursor.execute(sql)
        data = cursor.fetchall()
        courses = []
        for i in data:
            course = {'code': i[0], 'name': i[1], 'credits': i[2]}
            courses.append(course)
        return jsonify({'courses': courses, 'message': 'courses listed!'})
    except Exception as ex:
        return jsonify({'message': 'Error'})


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
