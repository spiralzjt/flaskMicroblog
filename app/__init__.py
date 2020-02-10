#with this file, python will seen app dir as a package
#and this file tell the app package to import other objects
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view='login'    # endpoint, /login URL

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models  #import at last to avoid circular imports