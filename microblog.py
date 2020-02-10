from app import app, db
from app.models import User, Post

#registers the function as a shell context function, When the flask shell command runs, it will invoke this function
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}