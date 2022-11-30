from flask import Flask, render_template, request, redirect, url_for, session,Blueprint,flash
from models.user import User
from models.forms import RegisterForm
from utils.db import db
from app import login_manager
from werkzeug.security import generate_password_hash
from flask_login import login_user, current_user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

users = Blueprint('users', __name__)

@users.route('/')
def inicio():
    return render_template('users/_home.html')
  
@users.route('/register', methods= ('GET', 'POST'))
def register():
    form = RegisterForm(meta ={'csrf': False})
    if form.validate_on_summit():
        if User.query.filter_by(username=form.username.data).first():
            flash('Usuario duplicado')
        else:
            users= User()
            users.username = form.username.data
            users.email = form.email.data
            users.password = generate_password_hash(form.password.data)
            db.session.add(users)
            db.session.commit()
            login_user(users, remember=True)
            return redirect(render_template('users/user.html'))
   
    
    if form.errors:
        flash('{{form.errors}}')
    return render_template('users/_sigin.html', form = form)
           