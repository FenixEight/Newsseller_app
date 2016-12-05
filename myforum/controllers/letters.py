from flask import request, session, redirect, url_for, flash
from myforum import app
from myforum.lib.template import render


@app.route('/letters', methods=['POST', 'GET'])
def letters():
    l = app.db.letter.get_all_letters()
    if request.method == 'POST':
        app.db.letter.add_letter(request.form['newsletter_name'], request.form['from_name'],
                                 request.form['from_email'], request.form['subject'],
                                 request.form['body_text'], request.form['body_html'])
        return redirect('letters')
    return render('letter', letters=l)


@app.route('/letters/edit/<int:id>', methods=['POST', 'GET'])
def edit_letter(id):
    letter = app.db.letter.get_letter(id)
    print letter
    if request.method == 'POST':
        app.db.letter.edit_letter(id, request.form['newsletter_name'],
                                  request.form['from_name'], request.form['from_email'],
                                  request.form['subject'], request.form['body_text'],
                                  request.form['body_html'])
        return redirect('letters')
    return render('edit_letter', letter=letter)


@app.route('/leters/delete/<int:id>', methods=['POST', 'GET'])
def delete_letter(id):
    if request.method == 'POST':
        app.db.letter.delete_letter(id)
    return redirect('letters')
