from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

from config import config
from validations import *

app = Flask(__name__)
connection = MySQL(app)


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Page not found, verify the URL</h1>", 404


@app.route('/courses', methods=['GET'])
def list_courses():
    try:
        cursor = connection.connection.cursor()
        sql = "SELECT * FROM course"
        cursor.execute(sql)
        data = cursor.fetchall()
        courses = [{'code': i[0], 'name': i[1], 'credits': i[2]} for i in data]
        return jsonify({'courses': courses, 'message': 'courses listed!'})
    except Exception as ex:
        return jsonify({'message': 'Error'})


@app.route('/courses/<code>', methods=['GET'])
def get_course(code):
    try:
        cursor = connection.connection.cursor()
        sql = "SELECT * FROM course WHERE code = %s"
        cursor.execute(sql, (code,))
        data = cursor.fetchone()
        if data is not None:
            course = {'code': data[0], 'name': data[1], 'credits': data[2]}
            return jsonify({'course': course, 'message': 'course found!'})
        else:
            return jsonify({'message': 'course not found!'})
    except Exception as ex:
        return jsonify({'message': 'Error'})


def get_course_bd(code):
    try:
        cursor = connection.connection.cursor()
        sql = "SELECT code, name, credits FROM course WHERE code = %s"
        cursor.execute(sql, (code,))
        data = cursor.fetchone()
        if data is not None:
            course = {'code': data[0], 'name': data[1], 'credits': data[2]}
            return course
        else:
            return None
    except Exception as ex:
        raise ex


@app.route('/courses', methods=['POST'])
def create_course():
    if (
        code_validation(request.json['code'])
        and name_validation(request.json['name'])
        and credits_validation(request.json['credits'])
    ):
        try:
            course = get_course_bd(request.json['code'])
            if course is not None:
                return jsonify({'message': "This code is already in use"})
            else:
                cursor = connection.connection.cursor()
                sql = """INSERT INTO course (code, name, credits)
                VALUES (%s, %s, %s)"""
                values = (
                    request.json['code'],
                    request.json['name'],
                    request.json['credits'],
                )
                cursor.execute(sql, values)
                connection.connection.commit()
                return jsonify({'message': 'course created'})
        except Exception as ex:
            return jsonify({'message': 'Error'})
    else:
        return jsonify({'message': "Invalid parameters for creating a course"})


@app.route('/courses/<code>', methods=['PUT'])
def update_course(code):
    if (
        code_validation(code)
        and name_validation(request.json['name'])
        and credits_validation(request.json['credits'])
    ):
        try:
            cursor = connection.connection.cursor()
            sql = """UPDATE course SET name = %s, credits = %s
            WHERE code = %s"""
            values = (
                request.json['name'],
                request.json['credits'],
                code,
            )
            cursor.execute(sql, values)
            connection.connection.commit()
            return jsonify({'message': 'course Updated'})
        except Exception as ex:
            return jsonify({'message': 'Error updating'})
    else:
        return jsonify({'message': "Invalid parameters for updating a course"})


@app.route('/courses/<code>', methods=['DELETE'])
def delete_course(code):
    try:
        cursor = connection.connection.cursor()
        sql = "DELETE FROM course WHERE code = %s"
        cursor.execute(sql, (code,))
        connection.connection.commit()
        return jsonify({'message': 'course deleted'})
    except Exception as ex:
        return jsonify({'message': 'Error'})


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
