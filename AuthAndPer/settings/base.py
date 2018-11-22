import os
from peewee_async import MySQLDatabase


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

settings = {
    "IP": "http://0.0.0.0:8888/",
    "db": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "mysql123",
        "name": "authandper",
        "port": 3306
    },
    "SECRET_KEY": "8mh1NU9l*1wWsGyqdsB9mv8lx6klKxVVI5uQ&2N9%2!vNVWgkvZ&NkED&cu9iL*d",
    "SECRET_EXPRIE": 7*24*3600,
    "JWT_AUTH_HEADER_PREFIX": "JWT"
}

database = MySQLDatabase('authandper', host="127.0.0.1", port=3306, user="root", password="mysql123")

