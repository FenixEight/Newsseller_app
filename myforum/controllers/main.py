import random
import xmlrpclib
from flask import request
from flask import url_for
from werkzeug.utils import redirect
from myforum import app
from myforum.lib.template import render
from myforum.model import Status


def get_proxy():
    return xmlrpclib.ServerProxy('http://localhost:8000')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        users = app.db.user.users()
        letter = app.db.letter.get_letter(request.form['select'])
        proxy = get_proxy()
        proxy.send_newsletter(letter, users)
    return render('home', letters=app.db.letter.get_all_letters())


@app.route('/stop', methods=['POST'])
def stop():
    proxy = get_proxy()
    proxy.stop()
    return redirect(url_for('home'))


@app.route('/resume', methods=['POST'])
def resume():
    proxy = get_proxy()
    proxy.resume()
    return redirect(url_for('home'))


@app.route('/reset', methods=['POST'])
def reset():
    proxy = get_proxy()
    proxy.reset()
    return redirect(url_for('home'))


@app.context_processor
def inject_build_num():
    proxy = get_proxy()
    status = Status()
    try:
        status_dict = proxy.get_state()
        status.status = status_dict['status']
        status.last_id = status_dict['last_id']
        status.error = status_dict['error']
    except BaseException:
        status.status = 'inaccessible'
    return dict(buildNum=random.randint(1, 123456), status=status)
