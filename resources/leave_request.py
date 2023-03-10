from flask_jwt_extended import (jwt_required, 
                                get_jwt_identity)
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from conn import conn, myCursor

from datetime import datetime

import pandas as pd

from schemas.leave_request import (LeaveRequestSchema, 
                                   LeaveRequestDetailSchema,
                                   LeaveRequestDeleteSchema,
                                   LeaveTypeSchema,
                                   LeaveReasonSchema,
                                   LeaveSupervisorSchema,
                                   LeaveEntitlementSchema,
                                   RequestDaySchema,
                                   LeaveRequestCreateSchema,
                                   LeaveRequestPermissionSchema,
                                   LeaveRequestUpdateSchema,
                                   LeaveRequestEmployeeSchema,
                                   LeaveRequestUnauthorizedSchema,
                                   LeaveRequestAuthorizeSchema,
                                   LeaveRequestDashboardSchema)

from models.leave_request_model import (LeaveRequestModel,
                                        LeaveRequestDetailModel,
                                        LeaveRequestTypeModel,
                                        LeaveRequestReasonModel,
                                        LeaveRequestSupervisorModel,
                                        LeaveRequestEntitlementModel,
                                        RequestDayModel,
                                        LeaveRequestCreateModel,
                                        LeaveRequestUpdateModel,
                                        LeaveRequestEmployeeModel,
                                        LeaveRequestUnauthorizedModel,
                                        LeaveRequestDashboardModel)

blp = Blueprint("Leave Request", __name__, description="Operation on LeaveRequest")

@blp.route('/leave-request/dashboard')
class LeaveRequestDashBoard(MethodView):
    @jwt_required()
    @blp.response(200, LeaveRequestDashboardSchema(many=True))
    @blp.doc(summary="Return a list of value by leave type")
    def get(self):
        try:
            user_id = get_jwt_identity()
            sql = """
            EXEC dbo.LeaveRequest_Dashboard 
                @UserID='{user_id}';
            """.format(user_id=user_id)
            
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching dashboard data")
        else:
            data = [LeaveRequestDashboardModel.from_json(item) for item in results.to_dict("records")]
            # data = [item for item in results.to_dict("records")]
            return data

@blp.route('/leave-request')
class LeaveRequest(MethodView):
    @jwt_required()
    @blp.response(200, LeaveRequestSchema(many=True))
    @blp.doc(summary="Return a list of Leave Request of logged in user")
    def get(self):
        user_id = get_jwt_identity()
        try:
            sql = """
            EXEC dbo.LeaveRequest_ListView 
                @userid='{user_id}';
            """.format(user_id=user_id)
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching Leave Requests.")
        else:
            data = [LeaveRequestModel.from_json(item) for item in results.to_dict("records")]
            
            return data
        
    @jwt_required()
    @blp.arguments(LeaveRequestCreateSchema)
    @blp.response(201, LeaveRequestCreateSchema)
    @blp.doc(summary="Create LeaveRequest of logged in user")
    def post(self, req_data):
        try:
            user_id = get_jwt_identity()
            data = LeaveRequestCreateModel.from_json(req_data)
            
            sql = """
            EXEC [dbo].[LeaveRequest_Add] 
                @EmployeeID=?, 
                @LTypeID=?, 
                @ValueDate=?, 
                @LeaveFrom=?, 
                @LeaveTo=?, 
                @NumReq=?, 
                @NumType=?, 
                @ReasonType=?, 
                @Remarks=?, 
                @UserID=?, 
                @retval=OUTPUT, 
                @AssignID=?;
            """
            
            values = (
                data.employee_id,
                data.leave_type,
                data.value_date,
                data.from_date,
                data.to_date,
                data.number_of_request,
                data.type_of_number,
                data.reason_type,
                data.remarks,
                user_id,
                data.submit_to
            )
            
            myCursor.execute(sql, values)
        except Exception:
            abort(500, message="Error Occurred while creating Leave Request.")
        else:
            conn.commit()
            return {"message": "Created Successfully."}

    @jwt_required()
    @blp.arguments(LeaveRequestUpdateSchema)
    @blp.response(200, LeaveRequestUpdateSchema)
    @blp.doc(summary="Edit the selected LeaveRequest of logged in user")
    def put(self, req_data):
        try:
            sql = """
            EXEC dbo.LeaveRequest_Update 
                @RequestID=?, 
                @LTypeID=?, 
                @LeaveFrom=?, 
                @LeaveTo=?, 
                @ValueDate=?, 
                @NumReq=?, 
                @NumType=?, 
                @ReasonType=?, 
                @Remarks=?, 
                @StartTime=?, 
                @EndTime=?, 
                @UserID=?, 
                @AssignID=?, 
                @retval=OUTPUT;
            """
            user_id = get_jwt_identity()
            data = LeaveRequestUpdateModel.from_json(req_data)
            values = (
                data.request_id,
                data.leave_type,
                data.from_date,
                data.to_date,
                data.value_date,
                data.number_of_request,
                data.type_of_number,
                data.reason_type,
                data.remarks,
                data.start_time,
                data.end_time,
                user_id,
                data.submit_to
            )
            myCursor.execute(sql, values)
        except Exception as err:
            abort(500, message=f"{err}") # Error occurred while editing leave request.
        else:
            conn.commit()
            return {"message": "Updated Successfully."}

    @jwt_required()
    @blp.arguments(LeaveRequestDeleteSchema)
    @blp.response(200, LeaveRequestDeleteSchema)
    @blp.doc(summary="Delete the selected LeaveRequest of logged in user")
    def delete(self, req_data):
        try:
            user_id = get_jwt_identity()
            sql = """
            EXEC dbo.LeaveRequest_Remove 
                @RequestID=?, 
                @UserID=?, 
                @retval=OUTPUT;
            """
            values = (
                req_data['request_id'],
                user_id
            )
            myCursor.execute(sql, values)
        except Exception:
            abort(500, message="Error occurred while deleting LeaveRequest.")
        else:
            conn.commit()
            return {"message": "Deleted Successfully."}

@blp.route('/leave-request/employee')
class LeaveRequestEmployee(MethodView):
    @jwt_required()
    @blp.response(200, LeaveRequestEmployeeSchema)
    @blp.doc(summary="Return the Employee information of logged in user.")
    def get(self):
        user_id = get_jwt_identity()
        
        try:
            sql = """
            EXEC dbo.LeaveRequest_GetEmployee 
                @UserID='{user_id}';
            """.format(user_id=user_id)
            
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching Employee Information.")
        else:
            tmp = results.to_dict("records")[0]
            data = LeaveRequestEmployeeModel.from_json(json=tmp)
            
            return data

@blp.route('/leave-request/<int:leave_id>')
class LeaveRequestDetail(MethodView):
    @jwt_required()
    @blp.response(200, LeaveRequestDetailSchema)
    @blp.doc(summary="Return the information of the selected LeaveRequest by ID")
    def get(self, leave_id):
        try:
            sql = """
            EXEC [dbo].[LeaveRequest_GetByID] 
                @id={leave_id};
            """.format(leave_id=leave_id)
            result = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching data.")
        else:
            if not result.to_dict("records"):
                abort(404, message=f"No LeaveRequest with ID of {leave_id}.")
            item = result.to_dict("records")[0]
            leave_data = LeaveRequestDetailModel.from_json(json=item)

            return leave_data
        
@blp.route('/leave-request/unauthorized-list')
class LeaveRequestUnauthorizedList(MethodView):
    @jwt_required()
    @blp.response(200, LeaveRequestUnauthorizedSchema(many=True))
    @blp.doc(summary="Return a list of UnauthorizedLeaveRequest of the logged in user.")
    def get(self):
        try:
            sql = """
            EXEC dbo.LeaveRequest_UnauthorizedList;
            """
            result = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occured while fetching Unauthorized LeaveRequest List.")
        else:
            data = [LeaveRequestUnauthorizedModel.from_json(item) for item in result.to_dict("records")]
            return data

@blp.route('/leave-request/approve')
class LeaveRequestApprove(MethodView):
    @jwt_required()
    @blp.arguments(LeaveRequestAuthorizeSchema)
    @blp.response(200, LeaveRequestAuthorizeSchema)
    @blp.doc(summary="Approve the selected UnauthorizedLeaveRequest of logged in user")
    def post(self, req_data):
        try:
            user_id = get_jwt_identity() # Get current logged in user
            
            sql = """
            EXEC dbo.LeaveRequest_Approve 
                @RequestID=?, 
                @UserID=? ,
                @retval=OUTPUT;
            """
            
            values = (
                req_data['request_id'],
                user_id    
            )
            myCursor.execute(sql, values)
        except Exception as err:
            abort(500, message=f"{err}")
        else:
            conn.commit()
            return {"message": "LeaveRequest has been approved."}

@blp.route('/leave-request/reject')
class LeaveRequestReject(MethodView):
    @jwt_required()
    @blp.arguments(LeaveRequestAuthorizeSchema)
    @blp.response(200, LeaveRequestAuthorizeSchema)
    @blp.doc(summary="Reject the selected UnauthorizedLeaveRequest of logged in user.")
    def post(self, req_data):
        try:
            user_id = get_jwt_identity()
            sql = """
            EXEC LeaveRequest_Reject 
                @RequestID=?, 
                @UserID=?, 
                @retval=OUTPUT;
            """
            values = (
                req_data['request_id'],
                user_id
            )
            myCursor.execute(sql, values)
        except Exception as err:
            abort(500, message=f"{err}")
        else:
            conn.commit()
            return {"message": "LeaveRequest has been rejected."}
        
@blp.route('/leave-request/types')
class LeaveRequestType(MethodView):
    @jwt_required()
    @blp.response(200, LeaveTypeSchema(many=True))
    @blp.doc(summary="Return a list of LeaveRequest Types")
    def get(self):
        try:
            sql = """
            EXEC [dbo].[LeaveRequest_GetTypeList];
            """
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching LeaveTypes.")
        else:
            data = [LeaveRequestTypeModel.from_json(json=item) for item in results.to_dict("recrods")]

            return data
    
@blp.route('/leave-request/reasons')
class LeaveRequestReason(MethodView):
    @jwt_required()
    @blp.response(200, LeaveReasonSchema(many=True))
    @blp.doc(summary="Return a list of LeaveRequest Reasons")
    def get(self):
        try:
            sql = """
            EXEC [dbo].[LeaveRequest_GetReasonList];
            """
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching data.")
        else:
            data = []
            if results.to_dict("records"):
                data = [LeaveRequestReasonModel.from_json(item) for item in results.to_dict("records")]
            
            return data
    
@blp.route('/leave-request/supervisors')
class LeaveRequestSupervisor(MethodView):
    @jwt_required()
    @blp.response(200, LeaveSupervisorSchema(many=True))
    @blp.doc(summary="Return a list of LeaveRequest supervisors")
    def get(self):
        try:
            user_id = get_jwt_identity()
            sql = """
            EXEC [dbo].[LeaveRequest_GetSupervisorList] 
                @UserID='{user_id}';
            """.format(user_id=user_id)
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching data.")
        else:
            data = []
            if results.to_dict("records"):
                data = [LeaveRequestSupervisorModel.from_json(item) for item in results.to_dict("records")]

            return data
        
@blp.route('/leave-request/entitlement')
class LeaveEntitlement(MethodView):
    @jwt_required()
    @blp.arguments(LeaveEntitlementSchema)
    @blp.response(200, LeaveEntitlementSchema)
    @blp.doc(summary="Return the information of LeaveRequestEntitlement")
    def post(self, req_data):
        try:
            sql = """
            EXEC dbo.LeaveRequest_Entitlement 
                @EmployeeID='{employee_id}', 
                @LTypeID='{l_type_id}', 
                @CurrentDate='{current_date}';
            """.format(**req_data, current_date=datetime.now().strftime("%Y-%m-%d"))
            results = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message="Error occurred while fetching data.")
        else:
            item = results.to_dict("records")[0]
            
            data = LeaveRequestEntitlementModel.from_json(item)
            
            return data

@blp.route('/leave-request/request-day')
class RequestDay(MethodView):
    @jwt_required()
    @blp.arguments(RequestDaySchema)
    @blp.response(200, RequestDaySchema)
    @blp.doc(summary="Get LeaveRequestDay", description="Get Number of Days based on StartDate & EndDate")
    def post(self, req_data):
        try:
            sql = """
            EXEC [dbo].[LeaveRequest_RequestDay] 
                @employeeid='{employee_id}', 
                @ltypeid='{l_type_id}', 
                @startdate='{leave_from}', 
                @enddate='{leave_to}';
            """.format(**req_data)
            results = pd.read_sql_query(sql, conn)
        except Exception as err:
            abort(500, message=f"{err}")
        else:
            item = results.to_dict("records")[0]
            data = RequestDayModel.from_json(item)
            
            return data

@blp.route('/leave-request/verify-permission')
class VerifyPermission(MethodView):
    @jwt_required()
    @blp.arguments(LeaveRequestPermissionSchema)
    @blp.response(200, LeaveRequestPermissionSchema)
    @blp.response(403, LeaveRequestPermissionSchema)
    @blp.doc(summary="Verify permission for logged in user. (Add, Edit, Delete, Authorize)")
    def post(self, req_data):
        permission_type = ["N", "E", "V", "D", "Q", "P", "R", "I", "X", "A"]
        if req_data['type_id'].upper() not in permission_type:
            abort(400, message="Invalid Permission Type")
        try:
            user_id = get_jwt_identity()
            sql = """
            DECLARE @return nvarchar(max) 
            EXEC dbo.LeaveRequest_VerifyPermission 
                @TypeID=?, 
                @UserID=?, 
                @RemoteAddr=?, 
                @retval=@return output; 
            SELECT @return; 
            """.format(**req_data)
            values = (
                req_data['type_id'],
                user_id,
                str(req_data['remote_addr'])
            )
            myCursor.execute(sql, values)
        except Exception:
            abort(500, message="Error occurred while verifying permission.")
        else:
            result = myCursor.fetchone()
            if len(result[0]) == 0:
                return {"message": "Permission verified."}, 200
            else:
                return {"message": "Permission denied."}, 403
