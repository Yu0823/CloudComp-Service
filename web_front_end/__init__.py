from flask import Flask
UPLOAD_FOLDER = '.'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

from web_front_end import main