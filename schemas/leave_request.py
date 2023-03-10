from marshmallow import Schema, fields

class LeaveRequestSchema(Schema):
    id = fields.Int(dump_only=True)
    auth_status = fields.Str(dump_only=True)
    request_id = fields.Str(dump_only=True)
    request_date = fields.Str(dump_only=True)
    request_type = fields.Str(dump_only=True)
    request_from = fields.Str(dump_only=True)
    request_to = fields.Str(dump_only=True)
    request_day = fields.Float(dump_only=True)
    status = fields.Str(dump_only=True)
    next_status = fields.Str(dump_only=True)
    assign = fields.Str(dump_only=True)
    post_date = fields.Str(dump_only=True)
    
class LeaveRequestDetailSchema(Schema):
    id = fields.Int(dump_only=True)
    employee_id = fields.Str(dump_only=True)
    employee_name = fields.Str(dump_only=True)
    leave_type_id = fields.Str(dump_only=True)
    leave_type = fields.Str(dump_only=True)
    request_date = fields.Str(dump_only=True)
    value_date = fields.Str(dump_only=True)
    yearly_leave_day = fields.Float(dump_only=True)
    up_to_date_bal_day = fields.Float(dump_only=True)
    seniority_day = fields.Float(dump_only=True)
    taken_bal_day = fields.Float(dump_only=True)
    last_year_bal_day = fields.Float(dump_only=True)
    maximum_bal_day = fields.Float(dump_only=True)
    request_from_date = fields.Str(dump_only=True)
    request_to_date = fields.Str(dump_only=True)
    number_of_request = fields.Float(dump_only=True)
    type_of_number = fields.Str(dump_only=True)
    type_of_number_desc = fields.Str(dump_only=True)
    reason_type = fields.Str(dump_only=True)
    reason_desc = fields.Str(dump_only=True)
    submit_to_id = fields.Int(dump_only=True)
    submit_to = fields.Str(dump_only=True)
    remarks = fields.Str(dump_only=True)
    request_id = fields.Str(dump_only=True)
    auth_status = fields.Str(dump_only=True)
    status_type = fields.Str(dump_only=True)
    status_desc = fields.Str(dump_only=True)
    
class LeaveTypeSchema(Schema):
    code = fields.Str(required=True, dump_only=True)
    name = fields.Str(required=True, dump_only=True)

class LeaveReasonSchema(Schema):
    code = fields.Str(required=True, dump_only=True)
    name = fields.Str(required=True, dump_only=True)

class LeaveSupervisorSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    code = fields.Str(required=True, dump_only=True)
    short = fields.Str(required=True, dump_only=True)
    name = fields.Str(required=True, dump_only=True)
    job_title = fields.Str(required=True, dump_only=True)
    
class LeaveEntitlementSchema(Schema):
    annual_entitle = fields.Float(dump_only=True)
    balance = fields.Float(dump_only=True)
    bal_date = fields.Str(dump_only=True)
    current_date = fields.Str(dump_only=True)
    employee_id = fields.Str(required=True)
    end_date = fields.Str(dump_only=True)
    entitle = fields.Float(dump_only=True)
    extra_leave_day = fields.Int(dump_only=True)
    fiscal_end = fields.Str(dump_only=True)
    fiscal_start = fields.Str(dump_only=True)
    leave_date = fields.Str(dump_only=True)
    l_type_id = fields.Str(required=True)
    remain = fields.Float(dump_only=True)
    seniority = fields.Float(dump_only=True)
    start_date = fields.Str(dump_only=True)
    taken = fields.Float(dump_only=True)
    type_name = fields.Str(dump_only=True)
    yearly_day = fields.Float(dump_only=True)

class RequestDaySchema(Schema):
    employee_id = fields.Str(required=True)
    l_type_id = fields.Str(required=True)
    leave_from = fields.Str(required=True)
    leave_to = fields.Str(required=True)
    no_hol_day = fields.Str(dump_only=True)
    no_pub_day = fields.Str(dump_only=True)
    num_req = fields.Float(dump_only=True)
    num_type = fields.Str(dump_only=True)
    public_day = fields.Float(dump_only=True)
    sch_class_id = fields.Int(dump_only=True)
    work_day = fields.Float(dump_only=True)
    holiday = fields.Float(dump_only=True)
    request_day = fields.Float(dump_only=True)
    request_hour = fields.Float(dump_only=True)

class LeaveRequestEmployeeSchema(Schema):
    employee_id = fields.Str(required=True, dump_only=True)
    full_name = fields.Str(required=True, dump_only=True)
    leave_date = fields.Str(required=True, dump_only=True)

class LeaveRequestCreateSchema(Schema):
    employee_id = fields.Str(required=True, load_only=True)
    leave_type = fields.Str(required=True, load_only=True)
    value_date = fields.Str(required=True, allow_none=True, load_only=True)
    from_date = fields.Str(required=True, load_only=True)
    to_date = fields.Str(required=True, load_only=True)
    number_of_request = fields.Int(required=True, load_only=True)
    type_of_number = fields.Str(required=True, load_only=True)
    reason_type = fields.Str(required=True, load_only=True)
    remarks = fields.Str(required=True, allow_none=True, load_only=True)
    submit_to = fields.Int(required=True, allow_none=True, load_only=True)
    message = fields.Str(required=True, dump_only=True)

class LeaveRequestUpdateSchema(Schema):
    request_id = fields.Str(required=True, load_only=True)
    leave_type = fields.Str(required=True, load_only=True)
    from_date = fields.Str(required=True, load_only=True)
    to_date = fields.Str(required=True, load_only=True)
    value_date = fields.Str(required=True, load_only=True)
    reason_type = fields.Str(required=True, allow_none=True, load_only=True)
    remarks = fields.Str(required=True, allow_none=True, load_only=True)
    start_time = fields.Str(required=True, allow_none=True, load_only=True)
    end_time = fields.Str(required=True, allow_none=True, load_only=True)
    submit_to = fields.Int(required=True, allow_none=True, load_only=True)
    number_of_request = fields.Int(required=True, load_only=True)
    type_of_number = fields.Str(required=True, load_only=True)
    message = fields.Str(required=True, dump_only=True)

class LeaveRequestDeleteSchema(Schema):
    request_id = fields.Str(required=True, load_only=True)
    message = fields.Str(required=True, dump_only=True)
    
class LeaveRequestPermissionSchema(Schema):
    type_id = fields.Str(required=True, load_only=True)
    remote_addr = fields.IPv4(required=True, load_only=True)
    message = fields.Str(required=True, dump_only=True)
    
class LeaveRequestUnauthorizedSchema(Schema):
    id = fields.Int(dump_only=True)
    staff_id = fields.Str(dump_only=True)
    request_id = fields.Str(dump_only=True)
    staff_name = fields.Str(dump_only=True)
    request_date = fields.Str(dump_only=True)
    position = fields.Str(dump_only=True)
    request_type = fields.Str(dump_only=True)
    request_from = fields.Str(dump_only=True)
    request_to = fields.Str(dump_only=True)
    num_day = fields.Float(dump_only=True)
    req_status = fields.Str(dump_only=True)
    next_status = fields.Str(dump_only=True)
    post_date = fields.Str(dump_only=True, allow_none=True)
    
class LeaveRequestAuthorizeSchema(Schema):
    request_id = fields.Str(required=True, load_only=True)
    message = fields.Str(required=True, dump_only=True)
    
class LeaveRequestDashboardSchema(Schema):
    name = fields.Str(required=True, dump_only=True)
    value = fields.Int(required=True, dump_only=True)
    