from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt

from app.auth.forms import LoginForm, SignUpForm
from app.models import User
from app import app, db

bcrypt = Bcrypt(app)

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=True)
        next_page = request.args.get('next')
        flash(f'Welcome, {user.username}')
        return redirect(next_page if next_page else url_for('main.homepage'))


    return render_template('login.html', form=form)
    
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash('Account Created.')
        return redirect(url_for('auth.login'))
    
    return render_template('signup.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    flash(f'{current_user.username} has been logged out')
    logout_user()
    return redirect(url_for('main.homepage'))
