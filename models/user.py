from utils.db import db


class User(db.Model) :
    """
    diseño y creacion de la tabla donde iran la informacion
    de los usuarios  en la base de datos 
    """
    
    __tablename__='user'
    
    id_user = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    borrow_days = db.Column(db.Integer)
    debt = db.Column(db.Float)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, first_name, last_name, borrow_days, debt, email,password) : 
        self.first_name = first_name
        self.last_name = last_name
        self.borrow_days = borrow_days
        self.debt = debt
        self.email = email
        self.password = password
