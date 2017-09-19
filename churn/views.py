import os
from flask import render_template
from churn import application
from churn import churn_form

basedir = os.path.abspath(os.path.dirname(__file__))


@application.route('/')
def home():
    print("inside home method")
    form = churn_form.ChurnForm()
    return render_template('churn_form.html', form=form)
