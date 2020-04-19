from flask import Flask, jsonify
from src.routes import api_routes

from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "KYS in 2 days"
    }
)

app = Flask(__name__)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
app.register_blueprint(api_routes)
