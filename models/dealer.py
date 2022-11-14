from utils.db import db


class User(db.Model) :
    """
    diseño y creacion de la tabla donde iran la informacion
    de los Documentos en la base de datos 
    """
    __tablename__= 'dealer'
    id_dealer = db.Column(db.Integer, primary_key=True)
    dealer_name = db.Column(db.String(100))
    units = db.Column(db.Integer)
    doc_name = db.Column(db.String(100))
    doc_type = db.Column(db.String(100))
    doc_value = db.Column(db.Float)

    def __init__(self, id_dealer, dealer_name, units, doc_name, doc_type, doc_value):
        self.id_dealer = id_dealer
        self.dealer_name = dealer_name
        self.units = units
        self.doc_name = doc_name
        self.doc_type = doc_type
        self.doc_value = doc_value
