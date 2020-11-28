from flask import render_template, redirect, url_for, session,flash
from app.auth import auth
from flask_login import logout_user, login_required


@auth.route('/login', methods=["GET", "POST"])
def login():
    return render_template('auth/login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('auth.login'))


@auth.route('/', methods=["GET", "POST"])
@login_required
def index():
    session['dash'] = 'active'
    return render_template('auth/dashboard.html', dash=session.get('dash'))