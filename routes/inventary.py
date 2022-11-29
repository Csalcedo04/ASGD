from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory
from models.doc import docs
from utils.db import db
from werkzeug.utils import secure_filename
import os

inventary = Blueprint("inventary", __name__)
inventary.add_url_rule(
    "/imagen/<filename>", endpoint="get_img", build_only=True
)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_DIRECTORY = 'file_img/'
@inventary.route('/inventary')
def index():
    document = docs.query.all()
   
    return render_template('index.html', document = document)

@inventary.route('/inventary/new_doc', methods=['POST'])
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
        daily_value = request.form['d_value']
        doc_type = request.form['doc_type']
        dealer_name = request.form['dealer']
        imagen = request.files['u_imagen']
        extension = os.path.splitext(imagen.filename)[1].lower() #se comprueba el tipo de documento
        #save image in a file 
        if imagen:
            if extension not in ALLOWED_EXTENSIONS:
                flash('no se anexo imagen', 'error')
            
            imagen.save(os.path.join(
                UPLOAD_DIRECTORY,
                secure_filename(imagen.filename)
            ))
        # create a new Contact object
        new_doc = docs( name, author, units, doc_type, value, daily_value, dealer_name)
       
        # save the object into the database
        db.session.add(new_doc)
        db.session.commit()
        
        flash('Document added successfully!')

        return redirect(url_for("inventary.index"))



@inventary.route("/inventary/update/<string:id>", methods=[ "GET","POST"])
def update(id):

    """
     funcion que recibe la data del formulario y actualiza los datos de un docuemnto
    en la DB, teniendo en cuenta el parametro de la ID del documento
    """
    # get document by id_document
    document = docs.query.get(id)

    if request.method == "POST":
        docs.doc_name = request.form['doc_name']
        docs.author = request.form['author']
        docs.units = request.form['doc_units']
        docs.doc_value = request.form['doc_value']
        docs.daily_value = request.form['d_value']
        docs.doc_type = request.form['doc_type']
        docs.dealer_name = request.form['dealer']
        #imagen = request.form['u_imagen']


        db.session.commit()

        flash('Document updated successfully!')

        return redirect(url_for('inventary.index'))
    
    return render_template("update.html", document=document)

@inventary.route("/inventary/delete/<id>", methods=["GET"])
def delete(id):
    """ funcion para borrar un objeto documento, teniendo en cuenta el parametro de la ID del documento"""
    document = docs.query.get(id)
    db.session.delete(document)
    db.session.commit()

    flash('Document deleted successfully!')

    return redirect(url_for("inventary.index"))


@inventary.route('/imagen/<filename>')
def get_img(filename):
    return send_from_directory( filename=UPLOAD_DIRECTORY + filename)