from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
# settings
login_manager = LoginManager(app)
app.secret_key = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Btv9p4EieLDDJP9qFj1V@containers-us-west-117.railway.app:6097/railway"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
 
SQLAlchemy(app)

#vistas

from routes.sell import sell
from routes.inventary import inventary
from routes.registro import users
app.register_blueprint(sell)
app.register_blueprint(inventary)
app.register_blueprint(users)
