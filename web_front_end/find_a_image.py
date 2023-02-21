from web_front_end import app
from flask import Flask, flash, request, redirect, url_for,  render_template
#import requests

@app.route('/find', methods=['GET', 'POST'])
def find_image():
    if request.method == 'POST':
        key = request.form.get("fname")
        if not key:
            flash('No key part')
            return render_template('show_image.html', value='please enter the key value')
        # has key, look into cache
        #r = requests.get("http://127.0.0.1:5002/api")
        #print(r.json())
        #if image in cache no found,
        #we look at the DB get the key and address of the file
        address = key_to_dir(key)
        if address:
            #show image!
            return render_template('show_image.html', image= address)

    return render_template('show_image.html')

def key_to_dir(key):
    if key:
        return 'te-kittens-cat-kitten-cats.jpeg'
    return
