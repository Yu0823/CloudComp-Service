from flask import Flask
from config import DB, DB_USER, DB_PSWD, DB_PORT, IP_EC2
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
UPLOAD_FOLDER = '.'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

class DBconfig(object):
    config_str = f'mysql://{DB_USER}:{DB_PSWD}@{IP_EC2}:{DB_PORT}/{DB}'
    print(config_str)
    app.config['SQLALCHEMY_DATABASE_URI'] = config_str

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False

app.config.from_object(DBconfig)
db = SQLAlchemy(app)

# class Role(db.Model):
#     # 定义表名
#     __tablename__ = 'roles'
#     # 定义字段
#     id = db.Column(db.Integer, primary_key=True,autoincrement=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User',backref='role') # 反推与role关联的多个User模型对象
#
# class User(db.Model):
#     # 定义表名
#     __tablename__ = 'users'
#     # 定义字段
#     id = db.Column(db.Integer, primary_key=True,autoincrement=True)
#     name = db.Column(db.String(64), unique=True, index=True)
#     email = db.Column(db.String(64),unique=True)
#     pswd = db.Column(db.String(64))
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 设置外键

with app.app_context():
    db.create_all()

from web_front_end import main

