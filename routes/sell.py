from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.doc import docs
from models.user import User
from utils.db import db

sell = Blueprint("sell", __name__)
@sell.route('/home')
def homepage():
    document = docs.query.all()
    return render_template('users/user.html', document=document)


@sell.route("/buy/<string:id>", methods=[ "POST","GET"])
def buy(id):
    # get id by id_document
    document = docs.query.get(id)
    if request.method == "POST":
        """primero se comprueba que aun existan unidades"""
        units = request.form['doc_units']
        """se resta la unidad que fue comprada y se pide el numero de dias que tendra con
        el producto y de ello se deduce el valor a pagar"""
        docs.units = docs.units - units
        User.debt = User.debt + docs.doc_value
        db.session.commit()
        flash ('Compra exitosa')
        return redirect(url_for('sell.homepage'))
    return render_template("users/_buying.html", document = document)

@sell.route("/borrow/<string:id>", methods=[ "POST","GET"])
def borrow(id):
    # get id by id_document
    document = docs.query.get(id)
    User.debt=1 
    
    if request.method == "POST":
        """primero se comprueba que aun existan unidades"""
      
        """se resta la unidad que fue comprada y se pide el numero de dias que tendra con
            el producto y de ello se deduce el valor a pagar"""
        User.borrow_days = request.form['doc_units']
        docs.units = docs.units - 1
        User.debt = User.debt * docs.daily_value
        db.session.commit()

        return redirect(url_for('sell.homepage'))
        
    return render_template("users/_borrow.html", document=document)

