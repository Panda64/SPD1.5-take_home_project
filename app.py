import jinja2
import os
import requests 

from dotenv import load_dotenv
from flask import Flask, render_template, request  


app = Flask(__name__)

# Get the API key from the '.env' file
load_dotenv()
API_KEY = os.getenv('API_KEY')


@app.route('/')
def home():
    return render_template('location.html')

@app.route('/mood')
def mood():
    zip_code = request.args.get('location')

    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'appid': API_KEY,
        'q': zip_code,
        'units': 'imperial'
    }

    weather = requests.get(url, params=params).json()

    return render_template('mood.html', weather=weather)

@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)