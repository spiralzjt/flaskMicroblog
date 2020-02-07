from app import app
from flask import render_template
from app.forms import LoginForm

#修饰器decorator，when a web browser requests either of these two URLs,
#Flask is going to invoke this function and pass the return value of it back to the browser as a response
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Zjt'}
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
    return render_template('index.html', title='home', user=user, posts = posts)
    #This function takes a template filename and a variable list of template arguments and returns the same template, but with all the placeholders in it replaced with actual values.


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)