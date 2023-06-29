# API REST with Flask and MySql 

This  repository contains the source code from a REST API I made as a practice for the flask framework and MySQL.

the example I abstract here is a common Course Manager, you can Create, Read, Update and Delete, courses from a MySQL database I created in PhpMyadmin with:

```
CREATE DATABASE api_flask;

USE api_flask;

CREATE TABLE course (
    code CHAR(6) PRIMARY KEY,
    name VARCHAR(30),
    credits TINYINT(1)
);
```

# Demo
I used Postman to test the project.

## Create
![image](https://github.com/m1gue21/api_flask_mysql/assets/73451596/1795111e-4ba8-4665-a662-e8b5b500af2d)


## Read
![image](https://github.com/m1gue21/api_flask_mysql/assets/73451596/88c8961c-001d-4c5b-8de7-7c06227da1c3)


## Update 
![image](https://github.com/m1gue21/api_flask_mysql/assets/73451596/3c4d1578-169e-42f3-80b5-0f22ab4f2578)

## Delete 
![image](https://github.com/m1gue21/api_flask_mysql/assets/73451596/00e2e511-1391-43f4-9421-0e1aea25a27b)

