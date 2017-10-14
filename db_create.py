from churn import db
from churn.models import churn_data_from_user

db.create_all()

print("DB created.")