import re
import os
from flask import render_template, request, redirect, url_for, flash, session, current_app
from app.main import main
from app.main.forms import ContactForm


def check_for_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  # regex for validating email as input
    if re.search(regex, email):
        return True


@main.route('/', methods=["GET", "POST"])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('home.html', form=form)


@main.route('/tours-and-travel', methods=["GET", "POST"])
def tours():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('main.tours'))
    return render_template('tours.html', form=form)
