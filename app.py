from flask import Flask, jsonify, redirect
import pyodbc as po
from conn import conn
import pandas as pd
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST

from resources.user import blp as UserBlueprint
from resources.leave_request import blp as LeaveRequestBlueprint
from resources.overtime_request import blp as OvertimeRequestBlueprint
from resources.payslip import blp as PayslipBlueprint

app = Flask(__name__)

app.config['API_TITLE'] = "HRMS System REST API"
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = "3.0.3"
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

app.config['JWT_SECRET_KEY'] = "273400726116270771902746508700512837087"
jwt = JWTManager(app)

"""
These methods use to modify the Error response about the Authorization
"""

# Check if the access token is in BLOCKLIST
@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload['jti'] in BLOCKLIST

# Return the response if the token has been revoked
@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({
            "description": "The access token has been revoked.",
            "error": "token_revoked"
        }),
        401
    )
    
# @jwt.needs_fresh_token_loader
# def token_not_fresh_callback(jwt_header, jwt_payload):
#     return (
#         jsonify({
#             "description": "The token is not fresh.",
#             "error": "fresh_token_required"
#         }),
#         401
#     )

# Add additional claims to refresh token so that the system can invalidate both access and refresh token at once
# @jwt.additional_claims_loader
# def add_claims_to_jwt(identity):
#     # Do sth in database to verify whether the user is admin or not
    
#     return {"is_admin": False}

# Requires to refresh token (NEED LEARNING)
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({"message": "The token has expired.", "error": "token_expired"}), 401)

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (jsonify({
        "message": "Signature verification failed.", "error": "invalid_token"
        }),
        401
    )

@jwt.unauthorized_loader
def missing_token_callback(error):
    return (jsonify({
        "description": "Request does not contain access token.",
        "error": "authorization_required."
    }), 401)

api.register_blueprint(UserBlueprint)
api.register_blueprint(LeaveRequestBlueprint)
api.register_blueprint(OvertimeRequestBlueprint)
api.register_blueprint(PayslipBlueprint)



@app.route('/')
def home():
    return redirect("/swagger-ui", code=302)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5006)