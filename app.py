from flask import Flask
from routes.sell import sell
from routes.inventary import inventary
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# settings
app.secret_key = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1234@localhost/docstoredb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)

app.register_blueprint(sell)
app.register_blueprint(inventary)
