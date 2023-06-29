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
![image](https://github.com/m1gue21/api_flask_mysql/assets/73451596/f0d6100b-2cf1-4846-b27e-7f9a93f491bc)

## Read
![image](https://github.com/m1gue21/api_flask_mysql/assets/73451596/d150257c-6d3e-44a9-9181-a09e0f737c7e)

## Update 
![image](https://github.com/m1gue21/api_flask_mysql/assets/73451596/8ffa36a4-9b75-4e8e-8afa-5ad837da68bc)

## Delete 
![image](https://github.com/m1gue21/api_flask_mysql/assets/73451596/f98b3c1d-6fb9-49b0-92f9-97eba005ec9a)
