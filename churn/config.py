import os

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
print("Database URI is: " + SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True

SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'