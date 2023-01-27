from flask import render_template, url_for, request
from memcache import webapp, memcache
from memcache.utils import basic_res, build_res
from flask_sqlalchemy import SQLAlchemy
import pymysql

@webapp.route('/')
def main():
    return render_template("main.html")

@webapp.route('/get',methods=['POST'])
def get():
    key = request.form.get('key')

    if key in memcache:
        value = memcache[key]
        response = build_res(200, value)
    else:
        response = build_res(400, "Unknown key")

    return response

@webapp.route('/put',methods=['POST'])
def put():
    key = request.form.get('key')
    value = request.form.get('value')
    memcache[key] = value

    return basic_res()

@webapp.route('/clear')
def clear():
    memcache.clear()

    return basic_res()

@webapp.route('/invalid', methods=['POST'])
def invalidate_key():
    key = request.form.get('key')
    memcache.pop(key)

    return basic_res()

@webapp.route('/refresh')
def refresh_configuration():
    #TODO: Load from database

    return basic_res()

@webapp.route('/show_keys')
def show_keys():
    pass

