"""from utils.db import db


class dealer(db.Model):

    __tablename__= 'dealer'
    id_dealer = db.Column(db.Integer, primary_key=True)
    dealer_name = db.Column(db.String(100), nullable= True)
    

    def __init__(self, dealer_name):
        self.dealer_name = dealer_name"""