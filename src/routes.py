from flask import Blueprint

api_routes = Blueprint('account_api', __name__)

@api_routes.route("/")
def hello():
    return "Ok Time to KYS"