from utils.db import db
from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin) :
    """
    diseño y creacion de la tabla donde iran la informacion
    de los usuarios  en la base de datos 
    """
    
    __tablename__='user'
    
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    borrow_days = db.Column(db.Integer)
    debt = db.Column(db.Float)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    def check_password(self, password):
        return check_password_hash(self.password, password)

    
