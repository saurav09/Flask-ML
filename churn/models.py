from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSON
from churn import db

class churn_data_from_user(db.Model):
    __tablename__ = "churn_form_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    State = Column(Integer)
    Account_Length = Column(Integer)
    Area_Code = Column(Integer)
    Intl_Plan = Column(Integer)
    VMail_Plan = Column(Integer)
    VMail_Message = Column(Integer)
    Day_Mins = Column(Integer)
    Day_Calls = Column(Integer)
    Eve_Mins = Column(Integer)
    Eve_Calls = Column(Integer)
    Night_Mins = Column(Integer)
    Night_Calls = Column(Integer)
    Intl_Mins = Column(Integer)
    Intl_Calls = Column(Integer)
    CustServ_Calls = Column(Integer)

    # def __init__(self, Account_Length):
    #     self.Account_Length = Account_Length

    def __repr__(self):
        return '<Account_Length {}>'.format(self.Account_Length)