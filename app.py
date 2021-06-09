import jinja2
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request  


app = Flask(__name__)

# Get the API key from the '.env' file
load_dotenv()
API_KEY = os.getenv('API_KEY')





if __name__ == '__main__':
    app.run(debug=True)