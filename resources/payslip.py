from flask_jwt_extended import (jwt_required, 
                                get_jwt_identity)
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from blocklist import BLOCKLIST
from conn import conn, myCursor

import pandas as pd


from models.payslip_model import PayslipModel

from schemas.payslip import PayslipSchema

blp = Blueprint("Payslip", __name__, description="Operations on Payslip")

@blp.route("/payslip")
class MyPayslip(MethodView):
    @jwt_required()
    @blp.response(200, PayslipSchema(many=True))
    def get(self):
        try:
            user_id = get_jwt_identity()
            sql = f"""
                EXEC dbo.MyPayslip_GetList 
	            @userid = '{user_id}';
            """
            results = pd.read_sql_query(sql, conn)
        
        except Exception:
            abort(500, message="Cannot get payslip data")
        
        else:
            data = []
            
            for item in results.to_dict("records"):
                data.append(PayslipModel.from_json(item))
            # data = [PayslipModel.from_json(item) for item in results.to_dict("records")]
            return data
        

# @blp.route("/payslip/dashboard")
# class MyPayslipDashboard(MethodView):
#     @jwt_required()
#     @blp.response(200, PayslipDashboardSchema(many=True))
#     def get(self):
#         try:
#             user_id = get_jwt_identity()
#             sql = f"""
#                 EXEC dbo.MyPayslip_Dashboard
# 	                @userid = {user_id};
#             """
            
#             result = pd.read_sql_query(sql, conn)
#         except Exception:
#             abort(500, "Cannot get payslip dashboard")
        
#         else:
#             data = []
