# Blueprint yapısı kullanılacak
from flask import Blueprint
from flask.templating import render_template, redirect, url_for
from functools import wraps
from service.auth import *

bp_auth=Blueprint('auth', __name__, url_prefix='/auth')

def login_required(f):
    @wraps(f)

    def is_access(*args, **kwargs):
        if not auth_service.is_logged():
            return redirect(url_for('auth.login'))
        else:
            return f(*args, **kwargs)
        
        return is_access


@bp_auth.route('/login', methods=['GET','POST'])

def login():
    return render_template('auth/login.html')