from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_wtf.csrf import CSRFProtect
from routes.contacts import contacts
from models.user_model import ModelUser
from models.user import User
from flask_login import LoginManager, login_user, logout_user
from utils.db import db


login = Blueprint('login', __name__)
csrf = CSRFProtect()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@login.route('/')
def index():
    return redirect(url_for('login.login_usuario'))

@login.route('/login', methods=['GET', 'POST'])
def login_usuario():
        
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('contacts.index'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')    
       
    else:
        return render_template('auth/login.html')
    
@login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.login_usuario'))

def status_401(error):
    return redirect(url_for('login.login_usuario'))

def status_405(error):
    return redirect(url_for('login.login_usuario'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404