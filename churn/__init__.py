from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = 'my-secrest-key'
app.config.from_pyfile('config.py')
db = SQLAlchemy()

from churn import views, models