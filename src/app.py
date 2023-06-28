from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

connection = MySQL(app)


def page_not_found(error):
    return "<h1>Page not found, verify the URL</h1>", 404


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


@app.route('/courses/<code>', methods=['GET'])
def get_course(code):
    try:
        cursor = connection.connection.cursor()
        sql = "SELECT * FROM course WHERE code = '{0}'".format(code)
        cursor.execute(sql)
        data = cursor.fetchone()
        if data is not None:
            course = {'code': data[0], 'name': data[1], 'credits': data[2]}
            return jsonify({'course': course, 'message': 'course found!'})
        else:
            return jsonify({'message': 'course not found!'})
    except Exception as ex:
        return jsonify({'message': 'Error'})


@app.route('/courses', methods=['POST'])
def create_course():
    try:
        cursor = connection.connection.cursor()
        sql = """INSERT INTO course (code, name, credits)
        VALUES ('{0}', '{1}', '{2}')""".format(request.json['code'], request.json['name'], request.json['credits'])
        cursor.execute(sql)
        connection.connection.commit()
        return jsonify({'message': 'course registered'})
    except Exception as ex:
        return jsonify({'message': 'Error'})


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
