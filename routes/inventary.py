from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.doc import docs
from utils.db import db

inventary = Blueprint("inventary", __name__)

@inventary.route('/')
def index():
    document = docs.query.all()
    return render_template('index.html', document=document)

@inventary.route('/new', methods=['POST'])
def add_contact():
    """
    funcion que recibe la data del formulario y la guarda en la DB
    
    """
    if request.method == 'POST':

        # receive data from the form
        name = request.form['doc_name']
        author = request.form['author']
        units = request.form['doc_units']
        value = request.form['doc_value']
        type = request.form['doc_type']

        # create a new Contact object
        new_doc = docs( name, author, units, type, value )

        # save the object into the database
        db.session.add(new_doc)
        db.session.commit()

        flash('Document added successfully!')

        return redirect(url_for("inventary.index"))


@inventary.route("/update/<id>", methods=[ "POST","GET"])
def update(id):

    """
     funcion que recibe la data del formulario y actualiza los datos de un docuemnto
    en la DB, teniendo en cuenta el parametro de la ID del documento
    """
    # get id by id_document
    document = docs.query.get(id)

    if request.method == "POST":
        docs.doc_name = request.form['doc_name']
        docs.author = request.form['author']
        docs.units = request.form['doc_units']
        docs.doc_value = request.form['doc_value']
        docs.doc_type = request.form['doc_type']

        db.session.commit()

        flash('Document updated successfully!')

        return redirect(url_for('inventary.index'))
    
    return render_template("update.html", document=document)


@inventary.route("/delete/<id>", methods=["GET"])
def delete(id):
    """ funcion para borrar un objeto documento, teniendo en cuenta el parametro de la ID del documento"""
    document = docs.query.get(id)
    db.session.delete(document)
    db.session.commit()

    flash('Document deleted successfully!')

    return redirect(url_for("inventary.index"))

