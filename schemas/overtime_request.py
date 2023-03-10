from marshmallow import Schema, fields

class OvertimeDashboardSchema(Schema):
    name = fields.Str(required=True, dump_only=True)
    value = fields.Int(required=True, dump_only=True)
    
class OvertimeRequestSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    request_type = fields.Str(required=True, dump_only=True)
    request_date = fields.Str(required=True, dump_only=True)
    request_from = fields.Str(required=True, dump_only=True)
    request_to = fields.Str(required=True, dump_only=True)
    request_hour = fields.Float(required=True, dump_only=True)
    request_status = fields.Str(required=True, dump_only=True)
    
class OvertimeByIDSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    employee_id = fields.Str(required=True, dump_only=True)
    request_id = fields.Str(required=True, dump_only=True)
    request_date = fields.Str(required=True, dump_only=True)
    overtime_date = fields.Str(required=True, dump_only=True)
    payment_date = fields.Str(required=True, dump_only=True, allow_none=True)
    start_date_time = fields.Str(required=True, dump_only=True)
    end_date_time = fields.Str(required=True, dump_only=True)
    num_hour = fields.Float(required=True, dump_only=True)
    hour_type = fields.Str(required=True, dump_only=True)
    hour_type_desc = fields.Str(required=True, dump_only=True)
    reason_type = fields.Str(required=True, dump_only=True, allow_none=True)
    reason_desc = fields.Str(required=True, dump_only=True, allow_none=True)
    assign_id = fields.Str(required=True, dump_only=True, allow_none=True)
    assign_name = fields.Str(required=True, dump_only=True, allow_none=True)
    remarks = fields.Str(required=True, dump_only=True, allow_none=True)
    status_type = fields.Str(required=True, dump_only=True)
    status_desc = fields.Str(required=True, dump_only=True)
    auth_status = fields.Str(required=True, dump_only=True)
    
class OvertimePermissionSchema(Schema):
    type_id = fields.Str(required=True, load_only=True)
    remote_addr = fields.IPv4(required=True, load_only=True)
    message = fields.Str(required=True, dump_only=True)
    
class OvertimeEmployeeSchema(Schema):
    employee_id = fields.Str(required=True, dump_only=True)
    full_name = fields.Str(required=True, dump_only=True)
    leave_date = fields.Str(required=True, dump_only=True)
    
class OvertimeTypeSchema(Schema):
    code = fields.Str(required=True, dump_only=True)
    name = fields.Str(required=True, dump_only=True)
    
class OvertimeReasonSchema(Schema):
    code = fields.Str(required=True, dump_only=True)
    name = fields.Str(required=True, dump_only=True)
    
class OvertimeSupervisorSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    code = fields.Str(required=True, dump_only=True)
    short = fields.Str(required=True, dump_only=True)
    name = fields.Str(required=True, dump_only=True)
    job_title = fields.Str(required=True, dump_only=True)
    
class OvertimeHourSchema(Schema):
    employee_id = fields.Str(required=True)
    start_time = fields.Str(required=True)
    end_time= fields.Str(required=True)
    work_day = fields.Float(required=True, dump_only=True)
    work_hour = fields.Float(required=True, dump_only=True)
    work_mins = fields.Float(required=True, dump_only=True)
    
class OvertimeCreateSchema(Schema):
    employee_id = fields.Str(required=True, load_only=True)
    request_date = fields.Str(required=True, load_only=True)
    overtime_date = fields.Str(required=True, load_only=True)
    start_time = fields.Str(required=True, load_only=True)
    end_time = fields.Str(required=True, load_only=True)
    num_hour = fields.Float(required=True, load_only=True)
    hour_type = fields.Str(required=True, load_only=True)
    reason_type = fields.Str(required=True, load_only=True, allow_none=True)
    remarks = fields.Str(required=True, load_only=True, allow_none=True)
    user_id = fields.Str(required=True, load_only=True)
    assign_id = fields.Int(required=True, load_only=True, allow_none=True)
    message = fields.Str(required=True, dump_only=True)
    
class OvertimeEditSchema(Schema):
    request_id = fields.Str(required=True, load_only=True)
    request_date = fields.Str(required=True, load_only=True)
    payment_date = fields.Str(load_only=True, allow_none=True)
    overtime_date = fields.Str(required=True, load_only=True)
    start_time = fields.Str(required=True, load_only=True)
    end_time = fields.Str(required=True, load_only=True)
    num_hour = fields.Float(required=True, load_only=True)
    hour_type = fields.Str(required=True, load_only=True)
    reason_type = fields.Str(required=True, load_only=True, allow_none=True)
    remarks = fields.Str(required=True, load_only=True, allow_none=True)
    user_id = fields.Str(required=True, load_only=True)
    assign_id = fields.Int(required=True, load_only=True, allow_none=True)
    message = fields.Str(required=True, dump_only=True)
    
class OvertimeDeleteSchema(Schema):
    request_id = fields.Str(required=True, load_only=True)
    message = fields.Str(required=True, dump_only=True)
    
class OvertimeAuthSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    request_type = fields.Str(required=True, dump_only=True)
    request_date = fields.Str(required=True, dump_only=True)
    request_from = fields.Str(required=True, dump_only=True)
    request_to = fields.Str(required=True, dump_only=True)
    request_hour = fields.Float(required=True, dump_only=True)
    request_status = fields.Str(required=True, dump_only=True)
    
class OvertimeApproveSchema(Schema):
    request_id = fields.Str(required=True, load_only=True)
    request_date = fields.Str(required=True, load_only=True)
    payment_date = fields.Str(required=True, load_only=True, allow_none=True)
    overtime_date = fields.Str(required=True, load_only=True)
    start_date_time = fields.Str(required=True, load_only=True)
    end_date_time = fields.Str(required=True, load_only=True)
    num_hour = fields.Float(required=True, load_only=True)
    hour_type = fields.Str(required=True, load_only=True)
    reason_type = fields.Str(required=True, load_only=True, allow_none=True)
    remarks = fields.Str(required=True, load_only=True, allow_none=True)
    assign_id = fields.Int(required=True, load_only=True, allow_none=True)
    user_id = fields.Str(required=True, load_only=True)
    message = fields.Str(required=True, dump_only=True)
    
class OvertimeRejectSchema(Schema):
    request_id = fields.Str(required=True, load_only=True)    
    assign_id = fields.Int(required=True, load_only=True, allow_none=True)
    message = fields.Str(required=True, dump_only=True)
    