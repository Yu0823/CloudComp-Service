from flask import render_template
#from app import

from web_front_end import app
import os
from flask import Flask, flash, request, redirect, url_for,  render_template
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif'}


@app.route('/')
def main():
    return "<p>Hello, World!</p>"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        key = request.form.get("fname")
        if not key:
            flash('No key part')
            return render_template('upload.html', value='please enter the key value')
        # check if the post request has the file part
        if 'file' not in request.files:
            print("break2")
            flash('No file part')
            #return redirect(request.url)
            return "<p>no file</p>"
        file = request.files['file']
        print("break3")
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            #if no file is broswd
            flash('No selected file')
            #return redirect(request.url)
            return render_template('upload.html', value='no file is selected')

        if file and allowed_file(file.filename) and key:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file', filename=filename))
            return "<p>upload!</p>"
    return render_template('upload.html')
