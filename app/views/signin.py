from flask import Blueprint

bp = Blueprint('signin', __name__, url_prefix='/signin')

@bp.route('/')  
def index():
    return "Hello, Sign In"