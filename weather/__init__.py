from flask import Blueprint

weather_bp = Blueprint('weather', __name__)

from . import routes