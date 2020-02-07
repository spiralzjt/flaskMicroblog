#with this file, python will seen app dir as a package
#and this file tell the app package to import other objects
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes  #import at last to avoid circular imports