import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config.from_object(os.environ['APP_SETTINGS'])
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# application.secret_key = 'my-secrest-key'
application.config.from_pyfile('../config.py')
db = SQLAlchemy(application)

from churn import views, models