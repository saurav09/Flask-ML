import os

import sys

import pandas as pd
from flask import render_template, request, jsonify
from churn import application, db, churn_form
from churn.models import churn_data_from_user
from sklearn.externals import joblib

basedir = os.path.abspath(os.path.dirname(__file__))

try:
    print("try", file=sys.stderr)
    print(basedir, file=sys.stderr)
    model = joblib.load(basedir + "/ml_model/churn_model.pkl")
    print("model loaded", file=sys.stderr)
except:
    print("No model found", file=sys.stderr)


@application.route('/')
def home():
    print("inside home method")
    form = churn_form.ChurnForm()
    return render_template('churn_form.html', form=form)


@application.route('/', methods=['post'])
def churn_form_data():
    churn_table = churn_data_from_user()
    churn_table.State = request.form['State']
    churn_table.Account_Length = request.form['Account_Length']
    churn_table.Area_Code = request.form['Area_Code']
    churn_table.Intl_Plan = request.form['Intl_Plan']
    churn_table.VMail_Plan = request.form['VMail_Plan']
    churn_table.VMail_Message = request.form['VMail_Message']
    churn_table.Day_Mins = request.form['Day_Mins']
    churn_table.Day_Calls = request.form['Day_Calls']
    churn_table.Eve_Mins = request.form['Eve_Mins']
    churn_table.Eve_Calls = request.form['Eve_Calls']
    churn_table.Night_Mins = request.form['Night_Mins']
    churn_table.Night_Calls = request.form['Night_Calls']
    churn_table.Intl_Mins = request.form['Intl_Mins']
    churn_table.Intl_Calls = request.form['Intl_Calls']
    churn_table.CustServ_Calls = request.form['CustServ_Calls']

    try:
        db.session.add(churn_table)
        db.session.commit()
    except:
        db.session.rollback()
        db.session.flush()

    db_data = churn_data_from_user()

    user = db_data.query.order_by('-id').first()
    print(user, file=sys.stdout)
    user = user.__dict__
    user.pop('_sa_instance_state', None)
    user.pop('id', None)
    print(user, file=sys.stdout)

    form = churn_form.ChurnForm()
    # print(request.form, file=sys.stderr)
    if form.validate_on_submit():
        prediction = churn_prediction(user)
        return jsonify({'prediction': int(prediction)})
    return jsonify(data=form.errors)
    # return "hello"


def churn_prediction(data):
    if model:
        test = pd.DataFrame([data])
        prediction = model.predict(test)[0]
        print(prediction, file=sys.stderr)
        return prediction
    else:
        return "model not found"
        data.pop('csrf_token', None)# postgresql://mlappdbaws:mlappdbaws@mlappdbaws.cwgdwgddyo6e.ap-south-1.rds.amazonaws.com:5432/mlAppDbAws
