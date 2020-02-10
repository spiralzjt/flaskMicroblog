from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import User

#修饰器decorator，when a web browser requests either of these two URLs,
#Flask is going to invoke this function and pass the return value of it back to the browser as a response
@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author' : {'username':'Jon'},
            'body' : 'Beautiful day in Singapore!'
        },
        {
            'author' : {'username' : 'Allen'},
            'body' : 'Driving a car in US is great!'
        }
    ]
    return render_template('index.html', title='home', posts = posts)
    #This function takes a template filename and a variable list of template arguments and returns the same template, but with all the placeholders in it replaced with actual values.


@app.route('/login', methods = ['GET', 'POST'])
def login():
    # if the user already logged in and access to /index dir, it gonna be redirected to /index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)