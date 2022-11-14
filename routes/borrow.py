from flask import Blueprint, render_template
from models.doc import Docs
from utils.db import db

borrow = Blueprint("borrow", __name__)





@borrow.route('/alquiler')
def index():
    document= Docs.query.all()
    return render_template('index.html', document=document)


@borrow.route('/catalogo/<string:doc_name>', methods=['GET'])
def get_doc():
    document = db.session.execute(db.select(Docs).order_by(Docs.doc_name)).scalars()
    return render_template("templates/sell.html", document=document)


@borrow.route("/catalogo/detalles/<int:id>")
def user_detail(id_document):
    document = db.get_or_404(Docs, id_document)
    return render_template("detalles/detail.html", document=document)

