import ZODB
from flask import Blueprint
from app import app

api_routes = Blueprint('account_api', __name__)
db = ZODB(app)

@app.before_request
def set_db_defaults():
    if 'entries' not in db:
        db['entries'] = List()


@api_routes.route("/")
def hello():
    return "Ok Time to KYS"