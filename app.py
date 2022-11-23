from flask import Flask, flash, request, redirect

from vendors.auth import check_pin_against_phone
from vendors.predictor import make_predictions
from vendors.utilities import save_file

app = Flask(__name__)


@app.route('/login')
def login():

    pin = request.form.get('pin')
    phone = request.form.get('phone')

    if None not in (pin, phone):
        return check_pin_against_phone(app, pin, phone)

    return None

@app.route('/predict', methods=['POST'])
def predict():

    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    file_path = save_file(file)

    prediction = make_predictions(file_path)

    return prediction


@app.route('/')
def index():
    return '''
        <!doctype html>
        <title>Upload Soil Image</title>
        <h1>Upload Soil Image</h1>
        <form action="/predict" method=post enctype=multipart/form-data>
          <input type=file name=file required>
          <input type=submit value=Upload>
        </form>
        '''