from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.contact import Contact 
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route("/listado")
@login_required
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts = contacts)

@contacts.route("/new", methods=['POST'])
def add_contact():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    new_contact = Contact(fullname, email, phone)
    db.session.add(new_contact)
    db.session.commit()
    flash('Contacto agregado satisfactoriamente')
    return redirect(url_for('contacts.index'))

@contacts.route("/update/<id>", methods=['POST', 'GET'])
@login_required
def update_contact(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
    
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        db.session.commit()
        flash('Contacto actualizado satisfactoriamente')
        return redirect(url_for('contacts.index'))
   
    
    return render_template('update.html', contact = contact)

@contacts.route("/delete/<id>")
@login_required
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contacto eliminado satisfactoriamente')
    return redirect(url_for('contacts.index'))

@contacts.route("/about")
@login_required
def about():
    return render_template('about.html')