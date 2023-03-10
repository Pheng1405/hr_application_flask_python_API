from flask_jwt_extended import (jwt_required, 
                                get_jwt_identity)
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from blocklist import BLOCKLIST
from conn import conn, myCursor

from datetime import datetime

import pandas as pd

from models.overtime_request_model import (OvertimeDashboardModel,
                                           OvertimeRequestModel,
                                           OvertimeEmployeeModel,
                                           OvertimeTypeModel,
                                           OvertimeReasonModel,
                                           OvertimeSupervisorModel,
                                           OvertimeHourModel,
                                           OvertimeCreateModel,
                                           OvertimeByIDModel,
                                           OvertimeEditModel,
                                           OvertimeDeleteModel,
                                           OvertimeAuthModel,
                                           OvertimeApproveModel,
                                           OvertimeRejectModel)

from schemas.overtime_request import (OvertimeDashboardSchema,
                                      OvertimeRequestSchema,
                                      OvertimePermissionSchema,
                                      OvertimeEmployeeSchema,
                                      OvertimeTypeSchema,
                                      OvertimeReasonSchema,
                                      OvertimeSupervisorSchema,
                                      OvertimeHourSchema,
                                      OvertimeCreateSchema,
                                      OvertimeByIDSchema,
                                      OvertimeEditSchema,
                                      OvertimeDeleteSchema,
                                      OvertimeAuthSchema,
                                      OvertimeApproveSchema,
                                      OvertimeRejectSchema)

blp = Blueprint("Overtime Requests", __name__, description="Operations on Overtime")

@blp.route('/overtime-request/dashboard')
class OvertimeRequestDashboard(MethodView):
    @jwt_required()
    @blp.doc(summary="Return Dashboard information by OvertimeType", description="Get Dashboard information by OvertimeTypes based on logged in User.")
    @blp.response(200, OvertimeDashboardSchema(many=True))
    def get(self):
        try:
            user_id = get_jwt_identity()
            sql = """
            EXEC dbo.OvertimeRequest_Dashboard 
                @UserID='{user_id}'
            """.format(user_id=user_id)
            
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching OvertimeDashboard data")
        else:
            data = [OvertimeDashboardModel.from_json(item) for item in results.to_dict("records")]
            
            return data
        
@blp.route('/overtime-request')
class OvertimeRequest(MethodView):
    @jwt_required()
    @blp.doc(summary="Return List of OvertimeRequests", description="Get List of OvertimeRequests of the logged in User.")
    @blp.response(200, OvertimeRequestSchema(many=True))
    def get(self):
        try:
            user_id = get_jwt_identity()
            
            sql = """
            EXEC OvertimeRequest_GetMobileRequestList 
                @UserID='{user_id}';
            """.format(user_id=user_id)
            
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching OvertimeRequests.")
        else:
            data = [OvertimeRequestModel.from_json(item) for item in results.to_dict("records")]
            return data
    
    @jwt_required()
    @blp.doc(summary="Create an OvertimeRequest", description="Add an OvertimeRequest record into the Database.")
    @blp.arguments(OvertimeCreateSchema)
    @blp.response(201, OvertimeCreateSchema)
    def post(self, req_data):
        try:
            overtime = OvertimeCreateModel.from_json(req_data)
            sql = """
            EXEC dbo.OvertimeRequest_Add 
                @EmployeeID=?, 
                @RequestDate=?, 
                @OvertimeDate=?, 
                @StartTime=?, 
                @EndTime=?, 
                @NumHour=?, 
                @HourType=?, 
                @ReasonType=?, 
                @Remarks=?, 
                @UserID=?, 
                @AssignID=?, 
                @retval=OUTPUT;
            """
            values = (
                overtime.employee_id,
                overtime.request_date,
                overtime.overtime_date,
                overtime.start_time,
                overtime.end_time,
                overtime.num_hour,
                overtime.hour_type,
                overtime.reason_type,
                overtime.remarks,
                overtime.user_id,
                overtime.assign_id
            )
            myCursor.execute(sql, values)
        except Exception:
            abort(500, message="Error occurred while creating OvertimeRequest.")
        else:
            conn.commit()
            return {"message": "Created successfully."}
            
    @jwt_required()
    @blp.doc(summary="Update an OvertimeRequest.", description="Update an OvertimeRequest record by the RequestID")
    @blp.arguments(OvertimeEditSchema)
    @blp.response(200, OvertimeEditSchema)
    def put(self, req_data):
        try:
            edit = OvertimeEditModel.from_json(req_data)
            sql = """
            EXEC dbo.OvertimeRequest_Update 
                @RequestID=?, 
                @RequestDate=?, 
                @PaymentDate=?, 
                @Overtimedate=?, 
                @StartTime=?, 
                @EndTime=?, 
                @NumHour=?, 
                @HourType=?, 
                @ReasonType=?, 
                @Remarks=?, 
                @UserID=?, 
                @AssignID=?, 
                @retval=OUTPUT;
            """
            values = (
                edit.request_id,
                edit.request_date,
                edit.payment_date,
                edit.overtime_date,
                edit.start_time,
                edit.end_time,
                edit.num_hour,
                edit.hour_type,
                edit.reason_type,
                edit.remarks,
                edit.user_id,
                edit.assign_id
            )
            myCursor.execute(sql, values)
        except Exception:
            abort(500, message="Error occurred while updating OvertimeRequest.")
        else:
            conn.commit()
            return {"message": "Updated successfully."}
        
    @jwt_required()
    @blp.doc(summary="Delete an OvertimeRequest.", description="Delete an OvertimeRequest record by the RequestID")
    @blp.arguments(OvertimeDeleteSchema)
    @blp.response(200, OvertimeDeleteSchema)
    def delete(self, req_data):
        try:
            user_id = get_jwt_identity()
            delete = OvertimeDeleteModel.from_json(req_data)
            sql = """
            EXEC dbo.OvertimeRequest_Remove 
                @RequestID=?,
                @UserID=?,
                @retval=OUTPUT;
            """
            values = (
                delete.request_id,
                user_id
            )
            myCursor.execute(sql, values)
        except Exception:
            abort(500, message="Error occurred while deleting OvertimeRequest.")
        else:
            conn.commit()
            return {"message": "Deleted successfully."}

@blp.route('/overtime-request/<int:id>')
class OvertimeRequestByID(MethodView):
    @jwt_required()
    @blp.doc(description="Return Overtime Detail based on ID", summary="Get Overtime by ID")
    @blp.response(200, OvertimeByIDSchema)
    def get(self, id):
        try:
            sql = """
            EXEC dbo.OvertimeRequest_GetByID 
                @ID={id};
            """.format(id=id)
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching data.")
        else:
            if not results.to_dict("records"):
                abort(404, message=f"No OvertimeRequest with ID of {id}.")
            item = results.to_dict("records")[0]
            data = OvertimeByIDModel.from_json(json=item)
            
            return data

@blp.route('/overtime-request/verify-permission')
class OvertimePermission(MethodView):
    @jwt_required()
    @blp.doc(description="Return message of User Permission", summary="Verify Permission of logged in user.")
    @blp.arguments(OvertimePermissionSchema)
    @blp.response(200, OvertimePermissionSchema)
    @blp.response(403, OvertimePermissionSchema)
    def post(self, req_data):
        permission_type = ["N", "E", "V", "D", "Q", "P", "R", "I", "X", "A"]
        if req_data['type_id'].upper() not in permission_type:
            abort(400, message="Invalid Permission Type")
        try:
            user_id = get_jwt_identity()
            sql= """
            DECLARE @return NVARCHAR(max); 
            EXEC dbo.OvertimeRequest_VerifyPermission 
                @TypeID=?, 
                @UserID=?, 
                @RemoteAddr=?, 
                @retval=@return OUTPUT; 
            SELECT @return;
            """
            values = (
                req_data['type_id'],
                user_id,
                str(req_data['remote_addr'])
            )
            myCursor.execute(sql, values)
        except Exception:
            abort(500, message="Error occurred while verifying user's permission.")
        else:
            result = myCursor.fetchone()
            if len(result[0]) == 0:
                return {"message": "Permission verified."}, 200
            else:
                return {"message": "Permission denied."}, 403
                
@blp.route('/overtime-request/employee')
class OvertimeRequestEmployee(MethodView):
    @jwt_required()
    @blp.response(200, OvertimeEmployeeSchema)
    @blp.doc(summary="Return the Employee information.", description="Get Employee information from database based on the logged in user.")
    def get(self):
        try:
            user_id = get_jwt_identity()
            sql = """
            EXEC dbo.OvertimeRequest_GetEmployee 
                @UserID='{user_id}';
            """.format(user_id=user_id)
            
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching Employee Information.")
        else:
            tmp = results.to_dict("records")[0]
            data = OvertimeEmployeeModel.from_json(json=tmp)
            
            return data
        
@blp.route('/overtime-request/types')
class OvertimeRequestType(MethodView):
    @jwt_required()
    @blp.doc(summary="Get Types of Overtime")
    @blp.response(200, OvertimeTypeSchema(many=True))
    def get(self):
        try:
            sql = "EXEC dbo.OvertimeRequest_GetTypeList;"
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error while fetching OvertimeTypes.")
        else:
            data = [OvertimeTypeModel.from_json(item) for item in results.to_dict("records")]
            return data
        
@blp.route('/overtime-request/reasons')
class OvertimeRequestReason(MethodView):
    @jwt_required()
    @blp.doc(summary="Get Overtime Reasons.")
    @blp.response(200, OvertimeReasonSchema(many=True))
    def get(self):
        try:
            sql = "EXEC dbo.OvertimeRequest_GetReasonList;"
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error while fetching OvertimeReasons.")
        else:
            data = [OvertimeReasonModel.from_json(item) for item in results.to_dict("records")]
            return data
        
@blp.route('/overtime-request/supervisors')
class OvertimeRequestSupervisor(MethodView):
    @jwt_required()
    @blp.doc(summary="Get List Supervisors of logged in user.")
    @blp.response(200, OvertimeSupervisorSchema(many=True))
    def get(self):
        try:
            user_id = get_jwt_identity()
            sql = """
            EXEC dbo.OvertimeRequest_GetSupervisorList 
                @UserID='{user_id}';
            """.format(user_id=user_id)
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error while fetching Supervisor List.")
        else:
            data = [OvertimeSupervisorModel.from_json(item) for item in results.to_dict("reocrds")]
            
            return data
        
@blp.route('/overtime-request/request-hour')
class OvertimeRequestHour(MethodView):
    @jwt_required()
    @blp.doc(description="Return number of hours based on start time and end time.", summary="Get Number of hours requested.")
    @blp.arguments(OvertimeHourSchema)
    @blp.response(200, OvertimeHourSchema)
    def post(self, req_data):
        try:
            sql = """
            DECLARE @return NVARCHAR(max);
            EXEC dbo.OvertimeRequest_GetHour 
                @EmployeeID='{employee_id}', 
                @StartTime='{start_time}', 
                @EndTime='{end_time}', 
                @retval=@return OUTPUT;
            """.format(**req_data)
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error while fetching OvertimeRequestHour.")
        else:
            item = results.to_dict("records")[0]
            data = OvertimeHourModel.from_json(item)
            
            return data
        
@blp.route('/overtime-request/unauthorized-list')
class OvertimeRequestAuth(MethodView):
    @jwt_required()
    @blp.doc(summary="Get Unauthorized OvertimeRequests.",
             description="Return List of Unauthorized OvertimeRequests.")
    @blp.response(200, OvertimeAuthSchema(many=True))
    def get(self):
        try:
            sql = "EXEC dbo.OvertimeRequest_GetMobileAuthList;"
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching data.")
        else:
            data = [OvertimeAuthModel.from_json(item) for item in results.to_dict("records")]
            return data 
        
@blp.route('/overtime-request/approve')
class OvertimeRequestApprove(MethodView):
    @jwt_required()
    @blp.doc(summary="Approve OvertimeRequests",
             description="Approve OvertimeRequest based on the given RequestID")
    @blp.arguments(OvertimeApproveSchema)
    @blp.response(200, OvertimeApproveSchema)
    def post(self, req_data):
        try:
            data = OvertimeApproveModel.from_json(req_data)
            sql = """
            EXEC dbo.OvertimeRequest_Approve 
                @RequestID=?, 
                @RequestDate=?, 
                @PaymentDate=?, 
                @OvertimeDate=?, 
                @StartTime=?, 
                @EndTime=?, 
                @NumHour=?, 
                @HourType=?, 
                @ReasonType=?, 
                @Remarks=?, 
                @AssignID=?, 
                @UserID=?, 
                @retval=OUTPUT;
            """
            values = (
                data.request_id,
                data.request_date,
                data.payment_date,
                data.overtime_date,
                data.start_date_time,
                data.end_date_time,
                data.num_hour,
                data.hour_type,
                data.reason_type,
                data.remarks,
                data.assign_id,
                data.user_id
            )
            myCursor.execute(sql, values)
        except Exception as err:
            abort(500, message=f"{err}")
        else:
            conn.commit()
            return {"message": "Overtime Approved."}
        
@blp.route('/overtime-request/reject')
class OvertimeRequestReject(MethodView):
    @jwt_required()
    @blp.doc(summary="Reject OvertimeRequests.",
             description="Reject OvertimeRequest based on the given RequestID.")
    @blp.arguments(OvertimeRejectSchema)
    @blp.response(200, OvertimeRejectSchema)
    def post(self, req_data):
        try:
            user_id = get_jwt_identity()
            data = OvertimeRejectModel.from_json(req_data)
            sql = """
            EXEC dbo.OvertimeRequest_Reject 
                @RequestID=?, 
                @UserID=?, 
                @AssignID=?, 
                @retval=OUTPUT;
            """
            values = (
                data.request_id,
                user_id,
                data.assign_id
            )
            myCursor.execute(sql, values)
        except Exception as err:
            abort(500, message=f"{err}")
        else:
            return {"message": "Overtime Rejected."}
            