import os

import sys
from flask import render_template, request
from churn import application, db, churn_form
from churn.models import churn_data_from_user

basedir = os.path.abspath(os.path.dirname(__file__))


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
    print(user, file=sys.stderr)
    user = user.__dict__
    user.pop('_sa_instance_state', None)
    user.pop('id', None)
    print(user, file=sys.stdout)

# postgresql://mlappdbaws:mlappdbaws@mlappdbaws.cwgdwgddyo6e.ap-south-1.rds.amazonaws.com:5432/mlAppDbAws