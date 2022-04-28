from flask import Flask
from flask_login import LoginManager
from routes.contacts import contacts
from routes.login import login
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from routes.login import login_manager

app = Flask(__name__)
app.secret_key = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)
login_manager.init_app(app)
app.register_blueprint(login)
app.register_blueprint(contacts)

