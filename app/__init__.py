from flask import Flask
from flask_bootstrap imoprt Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

from app import routes
