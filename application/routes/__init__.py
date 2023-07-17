
from flask import Blueprint

bp = Blueprint('views', __name__)

from application.routes import login, chat