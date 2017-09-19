import os
from flask import render_template
from churn import app
from churn import churn_form

basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/')
def home():
    form = churn_form.ChurnForm()
    return render_template('churn_form.html', form=form)
