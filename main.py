import os

import numpy
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

from predictor import prepare_image


UPLOAD_FOLDER = '/home/leber/PycharmProjects/soil_care_api/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/predict', methods=['POST'])
def predict():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        file_data = file.read()

        image_data, image = prepare_image(file_data)

        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return redirect(
            '/'
        )


@app.route("/")
def index():
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="/predict" method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''