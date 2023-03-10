class LeaveRequestModel:
    def __init__(
        self,
        id,
        auth_status,
        request_id,
        request_date,
        request_type,
        request_from,
        request_to,
        request_day,
        status,
        next_status,
        assign,
        post_date
    ):
        self.id = id
        self.auth_status = auth_status
        self.request_id = request_id
        self.request_date = request_date
        self.request_type = request_type
        self.request_from = request_from
        self.request_to = request_to
        self.request_day = request_day
        self.status = status
        self.next_status = next_status
        self.assign = assign
        self.post_date = post_date
        
    def __str__(self) -> dict:
        return {
            "id": self.id,
            "auth_status": self.auth_status,
            "request_id": self.request_id,
            "request_date": self.request_date,
            "request_type": self.request_type,
            "request_from": self.request_from,
            "request_to": self.request_to,
            "request_day": self.request_day,
            "status": self.status,
            "next_status": self.next_status,
            "assign": self.assign,
            "post_date": self.post_date
        }
        
    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestModel(
            id=json['ID'],
            auth_status=json['Auth Status'],
            request_id=json['Request ID'],
            request_date=json['Request Date'],
            request_type=json['Request Type'],
            request_from=json['Request From'],
            request_to=json['Request To'],
            request_day=json['Request Day'],
            status=json['Status'],
            next_status=json['Next Status'],
            assign=json['Assign'],
            post_date=json['Post Date']
        )
        
class LeaveRequestDetailModel:
    def __init__(
        self,
        id,
        employee_id,
        employee_name,
        leave_type_id,
        leave_type,
        request_date,
        value_date,
        yearly_leave_day,
        up_to_date_bal_day,
        seniority_day,
        taken_bal_day,
        last_year_bal_day,
        maximum_bal_day,
        request_from_date,
        request_to_date,
        number_of_request,
        type_of_number,
        type_of_number_desc,
        reason_type,
        reason_desc,
        submit_to_id,
        submit_to,
        remarks,
        request_id,
        auth_status,
        status_type,
        status_desc
    ):
        self.id = id
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.leave_type_id = leave_type_id
        self.leave_type = leave_type
        self.request_date = request_date
        self.value_date = value_date
        self.yearly_leave_day = yearly_leave_day
        self.up_to_date_bal_day = up_to_date_bal_day
        self.seniority_day = seniority_day
        self.taken_bal_day = taken_bal_day
        self.last_year_bal_day = last_year_bal_day
        self.maximum_bal_day = maximum_bal_day
        self.request_from_date = request_from_date
        self.request_to_date = request_to_date
        self.number_of_request = number_of_request
        self.type_of_number = type_of_number
        self.type_of_number_desc = type_of_number_desc
        self.reason_type = reason_type
        self.reason_desc = reason_desc
        self.submit_to_id = submit_to_id
        self.submit_to = submit_to
        self.remarks = remarks
        self.request_id = request_id
        self.auth_status = auth_status
        self.status_type = status_type
        self.status_desc = status_desc
        
    def __str__(self) -> dict:
        {
            "id": self.id,
            "employee_id": self.employee_id,
            "employee_name": self.employee_name,
            "leave_type_id": self.leave_type_id,
            "leave_type": self.leave_type,
            "request_date": self.request_date,
            "value_date": self.value_date,
            "yearly_leave_day": self.yearly_leave_day,
            "up_to_date_bal_day": self.up_to_date_bal_day,
            "seniority_day": self.seniority_day,
            "taken_bal_day": self.taken_bal_day,
            "last_year_bal_day": self.last_year_bal_day,
            "maximum_bal_day": self.maximum_bal_day,
            "request_from_date": self.request_from_date,
            "request_to_date": self.request_to_date,
            "number_of_request": self.number_of_request,
            "type_of_number": self.type_of_number,
            "type_of_number_desc": self.type_of_number_desc,
            "reason_type": self.reason_type,
            "reason_desc": self.reason_desc,
            "submit_to": self.submit_to,
            "remarks": self.remarks,
            "request_id": self.request_id,
            "auth_status": self.auth_status,
            "status_type": self.status_type,
            "status_desc": self.status_desc
        }
        
    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestDetailModel(
            id=json['ID'],
            employee_id=json['EmployeeID'],
            employee_name=json['FullName'],
            leave_type_id=json['LTypeID'],
            leave_type=json['TypeName'],
            request_date=json['RequestDate'].strftime("%Y-%m-%d"),
            value_date=json['ValueDate'].strftime("%Y-%m-%d"),
            yearly_leave_day=json['YearlyDay'],
            up_to_date_bal_day=json['Balance'],
            seniority_day=json['Seniority'],
            taken_bal_day=json['Taken'],
            last_year_bal_day=json['Remain'],
            maximum_bal_day=json['Entitlement'],
            request_from_date=json['LeaveFrom'].strftime("%Y-%m-%d"),
            request_to_date=json['LeaveTo'].strftime("%Y-%m-%d"),
            number_of_request=json['NumReq'],
            type_of_number=json['NumType'],
            type_of_number_desc=json['NumTypeDesc'],
            reason_type=json['ReasonType'],
            reason_desc=json['ReasonDesc'],
            submit_to_id=json['AssignID'],
            submit_to=json['AssignName'],
            remarks=json['Remarks'],
            request_id=json['RequestID'],
            auth_status=json['AuthStatus'],
            status_type=json['StatusType'],
            status_desc=json['StatusDesc']
        )
        
class LeaveRequestTypeModel:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        
    def __str__(self) -> dict:
        return {
            "code": self.code,
            "name": self.name
        }
    
    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestTypeModel(
            code=json['Code'],
            name=json['Name']
        )

class LeaveRequestReasonModel:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        
    def __str__(self) -> dict:
        return {
            "code": self.code,
            "name": self.name
        }
    
    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestReasonModel(
            code=json['Code'],
            name=json['Name']
        )

class LeaveRequestSupervisorModel:
    def __init__(
        self,
        id,
        code,
        short,
        name,
        job_title
    ):
        self.id = id
        self.code = code
        self.short = short
        self.name = name
        self.job_title = job_title
        
    def __str__(self) -> dict:
        return {
            "id": self.id,
            "code": self.code,
            "short": self.short,
            "name": self.name,
            "job_title": self.job_title
        }
    
    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestSupervisorModel(
            id=json['ID'],
            code=json['Code'],
            short=json['Short'],
            name=json['Name'],
            job_title=json['JobTitle']
        )
        
class LeaveRequestEntitlementModel:
    def __init__(
        self, 
        annual_entitle,
        balance,
        bal_date,
        current_date,
        employee_id,
        end_date,
        entitle,
        extra_leave_day,
        fiscal_end,
        fiscal_start,
        leave_date,
        l_type_id,
        remain,
        seniority,
        start_date,
        taken,
        type_name,
        yearly_day
    ):
        self.annual_entitle = annual_entitle
        self.balance = balance
        self.bal_date = bal_date
        self.current_date = current_date
        self.employee_id = employee_id
        self.end_date = end_date
        self.entitle = entitle
        self.extra_leave_day = extra_leave_day
        self.fiscal_end = fiscal_end
        self.fiscal_start = fiscal_start
        self.leave_date = leave_date
        self.l_type_id = l_type_id
        self.remain = remain
        self.seniority = seniority
        self.start_date = start_date
        self.taken = taken
        self.type_name = type_name
        self.yearly_day = yearly_day
    
    def __str__(self) -> dict:
        return {
            "annual_entitle": self.annual_entitle,
            "balance": self.balance,
            "bal_date": self.bal_date,
            "current_date": self.current_date,
            "employee_id": self.employee_id,
            "end_date": self.end_date,
            "entitle": self.entitle,
            "extra_leave_day": self.extra_leave_day,
            "fiscal_end": self.fiscal_end,
            "fiscal_start": self.fiscal_start,
            "leave_date": self.leave_date,
            "l_type_id": self.l_type_id,
            "remain": self.remain,
            "seniority": self.seniority,
            "start_date": self.start_date,
            "taken": self.taken,
            "type_name": self.type_name,
            "yearly_day": self.yearly_day
        }
        
    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestEntitlementModel(
            annual_entitle=json['annualentitle'],
            balance=json['balance'],
            bal_date=json['baldate'].strftime("%Y-%m-%d") if json['baldate'] else None,
            current_date=json['currentdate'].strftime("%Y-%m-%d") if json['baldate'] else None,
            employee_id=json['employeeid'],
            end_date=json['enddate'].strftime("%Y-%m-%d") if json['baldate'] else None,
            entitle=json['entitle'],
            extra_leave_day=json['extraleaveday'],
            fiscal_end=json['fiscalend'].strftime("%Y-%m-%d") if json['baldate'] else None,
            fiscal_start=json['fiscalstart'].strftime("%Y-%m-%d") if json['baldate'] else None,
            leave_date=json['leavedate'].strftime("%Y-%m-%d") if json['baldate'] else None,
            l_type_id=json['ltypeid'],
            remain=json['remain'],
            seniority=json['seniority'],
            start_date=json['startdate'].strftime("%Y-%m-%d") if json['baldate'] else None,
            taken=json['taken'],
            type_name=json['typename'],
            yearly_day=json['yearlyday'],
        )
        
class RequestDayModel:
    def __init__(
        self,
        employee_id,
        l_type_id,
        leave_from,
        leave_to,
        no_hol_day,
        no_pub_day,
        num_req,
        num_type,
        public_day,
        sch_class_id,
        work_day,
        holiday,
        request_day,
        request_hour
    ):
        self.employee_id = employee_id
        self.l_type_id = l_type_id
        self.leave_from = leave_from
        self.leave_to = leave_to
        self.no_hol_day = no_hol_day
        self.no_pub_day = no_pub_day
        self.num_req = num_req
        self.num_type = num_type
        self.public_day = public_day
        self.sch_class_id = sch_class_id
        self.work_day = work_day
        self.holidy = holiday
        self.request_day = request_day
        self.request_hour = request_hour
    
    def __str__(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "l_type_id": self.l_type_id,
            "leave_from": self.leave_from,
            "leave_to": self.leave_to,
            "no_hol_day": self.no_hol_day,
            "no_pub_day": self.no_pub_day,
            "num_req": self.num_req,
            "num_type": self.num_type,
            "public_day": self.public_day,
            "sch_class_id": self.sch_class_id,
            "work_day": self.work_day,
            "holiday": self.holidy,
            "request_day": self.request_day,
            "request_hour": self.request_hour
        }
        
    @classmethod
    def from_json(cls, json: dict):
        return RequestDayModel(
            employee_id=json['EmployeeID'],
            l_type_id=json['LTypeID'],
            leave_from=json['LeaveFrom'].strftime("%Y-%m-%d"),
            leave_to=json['LeaveTo'].strftime("%Y-%m-%d"),
            no_hol_day=json['NoHolDay'],
            no_pub_day=json['NoPubDay'],
            num_req=json['NumReq'],
            num_type=json['NumType'],
            public_day=json['PublicDay'],
            sch_class_id=json['SchClassID'],
            work_day=json['WorkDay'],
            holiday=json['holiday'],
            request_day=json['requstday'],
            request_hour=json['requsthour']
        )
       
class LeaveRequestEmployeeModel:
    def __init__(
        self,
        employee_id,
        full_name,
        leave_date
    ):
        self.employee_id = employee_id
        self.full_name = full_name
        self.leave_date = leave_date

    def __str__(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "full_name": self.full_name,
            "leave_date": self.leave_date
        }

    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestEmployeeModel(
            employee_id=json['EmployeeID'],
            full_name=json['FullName'],
            leave_date=json['LeaveDate'].strftime("%Y-%m-%d")
        )
    
class LeaveRequestCreateModel:
    def __init__(
        self,
        employee_id,
        leave_type,
        value_date,
        from_date,
        to_date,
        number_of_request,
        type_of_number,
        reason_type,
        remarks,
        submit_to
    ):
        self.employee_id = employee_id
        self.leave_type = leave_type
        self.value_date = value_date
        self.from_date = from_date
        self.to_date = to_date
        self.number_of_request = number_of_request
        self.type_of_number = type_of_number
        self.reason_type = reason_type
        self.remarks = remarks
        self.submit_to = submit_to
    
    def __str__(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "leave_type": self.leave_type,
            "value_date": self.value_date,
            "from_date": self.from_date,
            "to_date": self.to_date,
            "number_of_request": self.number_of_request,
            "type_of_number": self.type_of_number,
            "reason_type": self.reason_type,
            "remarks": self.remarks,
            "submit_to": self.submit_to
        }

    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestCreateModel(
            employee_id=json['employee_id'],
            leave_type=json['leave_type'],
            value_date=json['value_date'],
            from_date=json['from_date'],
            to_date=json['to_date'],
            number_of_request=json['number_of_request'],
            type_of_number=json['type_of_number'],
            reason_type=json['reason_type'],
            remarks=json['remarks'],
            submit_to=json['submit_to']
        )

class LeaveRequestUpdateModel:
    def __init__(
        self,
        request_id,
        leave_type,
        from_date,
        to_date,
        value_date,
        reason_type,
        remarks,
        start_time,
        end_time,
        submit_to,
        number_of_request,
        type_of_number
    ):
        self.request_id = request_id
        self.leave_type = leave_type
        self.from_date = from_date
        self.to_date = to_date
        self.value_date = value_date
        self.reason_type = reason_type
        self.remarks = remarks
        self.start_time = start_time
        self.end_time = end_time
        self.submit_to = submit_to
        self.number_of_request = number_of_request
        self.type_of_number = type_of_number
    
    def __str__(self) -> dict:
        return {
            "request_id": self.request_id,
            "leave_type": self.leave_type,
            "from_date": self.from_date,
            "to_date": self.to_date,
            "value_date": self.value_date,
            "reason_type": self.reason_type,
            "remarks": self.remarks,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "submit_to": self.submit_to,
            "number_of_request": self.number_of_request,
            "type_of_number": self.type_of_number
        }
    
    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestUpdateModel(
            request_id=json['request_id'],
            leave_type=json['leave_type'],
            from_date=json['from_date'],
            to_date=json['to_date'],
            value_date=json['value_date'],
            reason_type=json['reason_type'],
            remarks=json['remarks'],
            start_time=json['start_time'],
            end_time=json['end_time'],
            submit_to=json['submit_to'],
            number_of_request=json['number_of_request'],
            type_of_number=json['type_of_number']
        )

class LeaveRequestUnauthorizedModel:
    def __init__(
        self,
        id,
        staff_id,
        request_id,
        staff_name,
        request_date,
        position,
        request_type,
        request_from,
        request_to,
        num_day,
        req_status,
        next_status,
        post_date
    ):
        self.id = id
        self.staff_id = staff_id
        self.request_id = request_id
        self.staff_name = staff_name
        self.request_date = request_date
        self.position = position
        self.request_type = request_type
        self.request_from = request_from
        self.request_to = request_to
        self.num_day = num_day
        self.req_status = req_status
        self.next_status = next_status
        self.post_date = post_date

    def __str__(self) -> dict:
        return {
            "id": self.id,
            "staff_id": self.staff_id,
            "request_id": self.request_id,
            "staff_name": self.staff_name,
            "request_date": self.request_date,
            "position": self.position,
            "request_type": self.request_type,
            "request_from": self.request_from,
            "request_to": self.request_to,
            "num_day": self.num_day,
            "req_status": self.req_status,
            "next_status": self.next_status,
            "post_date": self.post_date
        }

    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestUnauthorizedModel(
            id=json['ID'],
            staff_id=json['Staff ID'],
            request_id=json['Request ID'],
            staff_name=json['Staff Name'],
            request_date=json['Request Date'],
            position=json['Position'],
            request_type=json['Request Type'],
            request_from=json['Request From'],
            request_to=json['Request To'],
            num_day=json['Num Day'],
            req_status=json['Req. Status'],
            next_status=json['Next Status'],
            post_date=json['Post Date']
        )
        
class LeaveRequestDashboardModel:
    def __init__(
        self,
        name,
        value
    ):
        self.name = name
        self.value = value

    def __str__(self) -> dict:
        return {
            "name": self.name,
            "value": self.value
        }

    @classmethod
    def from_json(cls, json: dict):
        return LeaveRequestDashboardModel(
            name=json['Name'],
            value=json['Value']
        )
    