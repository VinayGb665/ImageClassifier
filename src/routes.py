from flask import Blueprint
from app import db

api_routes = Blueprint('account_api', __name__)

@app.before_request
def set_db_defaults():
    if 'entries' not in db:
        db['entries'] = List()


@api_routes.route("/")
def hello():
    return "Ok Time to KYS"