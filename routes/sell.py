from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.doc import docs
from utils.db import db

sell = Blueprint("sell", __name__)

@sell.route('/user')
def index():
    document = docs.query.all()
    return render_template('user.html', document=document)
"""
 EN DESARROLLO

@sell.route("/buy/<id>", methods=[ "POST","GET"])
def buy(id):
    # get id by id_document
    document = docs.query.get(id)

    if request.method == "POST":
        docs.doc_name = request.form['doc_name']
        docs.author = request.form['author']
        docs.units = request.form['doc_units']
        docs.doc_value = request.form['doc_value']
        docs.doc_type = request.form['doc_type']

        db.session.commit()

        flash('Contact updated successfully!')

        return redirect(url_for('sell.index'))
    
    return render_template("user.html", document=document)


@sell.route("/delete/<id>", methods=["GET"])
def borrow(id):
    document = docs.query.get(id)
    db.session.delete(document)
    db.session.commit()

    flash('Contact deleted successfully!')

    return redirect(url_for("sell.index"))

"""
