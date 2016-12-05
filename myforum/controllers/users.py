import os
import random
import xmlrpclib

from flask import request, session, redirect, url_for, flash
from myforum import app
from myforum.lib.template import render

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        app.db.user.add_user(full_name, email)
    users_list = app.db.user.users()
    return render('user', users=users_list)

@app.route('/users/edit/<int:id>', methods=['POST', 'GET'])
def edit_user(id):
    user = app.db.user.get_user(id)
    if request.method == 'POST':
        app.db.user.edit_user(id, request.form['full_name'], request.form['email'])
        return redirect('users')
    return render('edit_user', user=user)

@app.route('/users/delete/<int:id>', methods=['POST'])
def delete_user(id):
    if request.method == 'POST':
        app.db.user.delete_user(id)
    return redirect('users')
