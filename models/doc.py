from utils.db import db


class docs(db.Model):
    """
    diseño y creacion de la tabla donde iran la informacion
    de los Documentos en la base de datos 
    """
    __tablename__='docs'
    id_ = db.Column(db.Integer, primary_key=True)
    doc_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100),nullable=False)
    units = db.Column(db.Integer, nullable=False)
    doc_value = db.Column(db.Float, nullable=False)
    daily_value = db.Column(db.Float, nullable=False)
    doc_type = db.Column(db.String(100),nullable=False)
    dealer_name = db.Column(db.String(100), nullable=True)




    def __init__(self, doc_name, author, units, doc_type, doc_value, daily_value,dealer_name):
        self.doc_name = doc_name
        self.author = author
        self.units = units
        self.doc_value = doc_value
        self.daily_value = daily_value
        self.doc_type = doc_type
        self.dealer_name = dealer_name
