from flask_wtf import FlaskForm
from wtforms import IntegerField


class ChurnForm(FlaskForm):
    State = IntegerField("State")
    Account_Length = IntegerField("Account_Length")
    Area_Code = IntegerField("Area_Code")
    Intl_Plan = IntegerField("Intl_Plan")
    VMail_Plan = IntegerField("VMail_Plan")
    VMail_Message = IntegerField("VMail_Message")
    Day_Mins = IntegerField("Day_Mins")
    Day_Calls = IntegerField("Day_Calls")
    Eve_Mins = IntegerField("Eve_Mins")
    Eve_Calls = IntegerField("Eve_Calls")
    Night_Mins = IntegerField("Night_Mins")
    Night_Calls = IntegerField("Night_Calls")
    Intl_Mins = IntegerField("Intl_Mins")
    Intl_Calls = IntegerField("Intl_Calls")
    CustServ_Calls = IntegerField("CustServ_Calls")
