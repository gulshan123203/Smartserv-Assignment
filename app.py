from flask import Flask, render_template
from preprocessing import func
import requests
import json
import pandas as pd

app = Flask(__name__)
URL = 'https://s3.amazonaws.com/open-to-cors/assignment.json'

def func(url):
    response = requests.get(url, "GET")
    if response.status_code == 200:
        json_object = json.loads(response.content)
        count = json_object['count']
        products = json_object['products']
        df = pd.DataFrame.from_dict(products.values())

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
    # return 'Hello World'


@app.route('/base', methods=['POST', 'GET'])
def base():
    json_data = func(URL)
    return render_template('base.html', tables=[json_data.to_html(classes='data')], titles=json_data.columns.values)


if __name__ == '__main__':
    app.run()



