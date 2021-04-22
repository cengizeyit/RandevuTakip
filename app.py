from flask import Flask, Response
from config import Config

app = Flask(__name__)

app.debug=True
app.secret_key='appopiiii'
app.config.from_object(Config)
