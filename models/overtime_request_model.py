class OvertimeDashboardModel:
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
        return OvertimeDashboardModel(
            name=json['Name'],
            value=json['Value']
        )
        
class OvertimeRequestModel:
    def __init__(
        self,
        id,
        request_type,
        request_date,
        request_from,
        request_to,
        request_hour,
        request_status
    ):
        self.id = id
        self.request_type = request_type
        self.request_date = request_date
        self.request_from = request_from
        self.request_to = request_to
        self.request_hour = request_hour
        self.request_status = request_status

    def __str__(self) -> dict:
        return {
            "id": self.id,
            "request_type": self.request_type,
            "request_date": self.request_date,
            "request_from": self.request_from,
            "request_to": self.request_to,
            "request_hour": self.request_hour,
            "request_status": self.request_status
        }

    @classmethod
    def from_json(cls, json: dict):
        return OvertimeRequestModel(
            id=json['ID'],
            request_type=json['RequestType'],
            request_date=json['RequestDate'],
            request_from=json['RequestFrom'],
            request_to=json['RequestTo'],
            request_hour=json['RequestHour'],
            request_status=json['RequestStatus']
        )

class OvertimeByIDModel:
    def __init__(
        self,
        id,
        employee_id,
        request_id,
        request_date,
        overtime_date,
        payment_date,
        start_date_time,
        end_date_time,
        num_hour,
        hour_type,
        hour_type_desc,
        reason_type,
        reason_desc,
        assign_id,
        assign_name,
        remarks,
        status_type,
        status_desc,
        auth_status
    ):
        self.id = id
        self.employee_id = employee_id
        self.request_id = request_id
        self.request_date = request_date
        self.overtime_date = overtime_date
        self.payment_date = payment_date
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.num_hour = num_hour
        self.hour_type = hour_type
        self.hour_type_desc = hour_type_desc
        self.reason_type = reason_type
        self.reason_desc = reason_desc
        self.assign_id = assign_id
        self.assign_name = assign_name
        self.remarks = remarks
        self.status_type = status_type
        self.status_desc = status_desc
        self.auth_status = auth_status

    def __str__(self) -> dict:
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "request_id": self.request_id,
            "request_date": self.request_date,
            "overtime_date": self.overtime_date,
            "payment_date": self.payment_date,
            "start_date_time": self.start_date_time,
            "end_date_time": self.end_date_time,
            "num_hour": self.num_hour,
            "hour_type": self.hour_type,
            "hour_type_desc": self.hour_type_desc,
            "reason_type": self.reason_type,
            "reason_desc": self.reason_desc,
            "assign_id": self.assign_id,
            "assign_name": self.assign_name,
            "remarks": self.remarks,
            "status_type": self.status_type,
            "status_desc": self.status_desc,
            "auth_status": self.auth_status
        }

    @classmethod
    def from_json(cls, json: dict):
        return OvertimeByIDModel(
            id=json['ID'],
            employee_id=json['EmployeeID'],
            request_id=json['RequestID'],
            request_date=json['RequestDate'].strftime("%Y-%m-%d"),
            overtime_date=json['OvertimeDate'].strftime("%Y-%m-%d"),
            payment_date=json['PaymentDate'] if json['PaymentDate'] else None,
            start_date_time=json['StartDateTime'].strftime("%Y-%m-%d %H:%M:%S"),
            end_date_time=json['EndDateTime'].strftime("%Y-%m-%d %H:%M:%S"),
            num_hour=json['NumHour'],
            hour_type=json['HourType'],
            hour_type_desc=json['HourTypeDesc'],
            reason_type=json['ReasonType'],
            reason_desc=json['ReasonDesc'],
            assign_id=json['AssignID'],
            assign_name=json['AssignName'],
            remarks=json['Remarks'],
            status_type=json['StatusType'],
            status_desc=json['StatusDesc'],
            auth_status=json['AuthStatus']
        )
        
class OvertimeEmployeeModel:
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
        return OvertimeEmployeeModel(
            employee_id=json['EmployeeID'],
            full_name=json['FullName'],
            leave_date=json['LeaveDate'].strftime("%Y-%m-%d")
        )
        
class OvertimeTypeModel:
    def __init__(
        self,
        code,
        name
    ):
        self.code = code
        self.name = name

    def __str__(self) -> dict:
        return {
            "code": self.code,
            "name": self.name
        }

    @classmethod
    def from_json(cls, json: dict):
        return OvertimeTypeModel(
            code=json['Code'],
            name=json['Name']
        )

class OvertimeReasonModel:
    def __init__(
        self,
        code,
        name
    ):
        self.code = code
        self.name = name

    def __str__(self) -> dict:
        return {
            "code": self.code,
            "name": self.name
        }

    @classmethod
    def from_json(cls, json: dict):
        return OvertimeReasonModel(
            code=json['Code'],
            name=json['Name']
        )

class OvertimeSupervisorModel:
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
        return OvertimeSupervisorModel(
            id=json['ID'],
            code=json['Code'],
            short=json['Short'],
            name=json['Name'],
            job_title=json['JobTitle']
        )
       
class OvertimeHourModel:
    def __init__(
        self,
        employee_id,
        start_time,
        end_time,
        work_day,
        work_hour,
        work_mins
    ):
        self.employee_id = employee_id
        self.start_time = start_time
        self.end_time = end_time
        self.work_day = work_day
        self.work_hour = work_hour
        self.work_mins = work_mins

    def __str__(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "work_day": self.work_day,
            "work_hour": self.work_hour,
            "work_mins": self.work_mins
        }

    @classmethod
    def from_json(cls, json: dict):
        return OvertimeHourModel(
            employee_id=json['EmployeeID'],
            start_time=json['StartTime'],
            end_time=json['EndTime'],
            work_day=json['WorkDay'],
            work_hour=json['WorkHour'],
            work_mins=json['WorkMins']
        )
        
class OvertimeCreateModel:
    def __init__(
        self,
        employee_id,
        request_date,
        overtime_date,
        start_time,
        end_time,
        num_hour,
        hour_type,
        reason_type,
        remarks,
        user_id,
        assign_id
    ):
        self.employee_id = employee_id
        self.request_date = request_date
        self.overtime_date = overtime_date
        self.start_time = start_time
        self.end_time = end_time
        self.num_hour = num_hour
        self.hour_type = hour_type
        self.reason_type = reason_type
        self.remarks = remarks
        self.user_id = user_id
        self.assign_id = assign_id

    def __str__(self) -> dict:
        return {
            "employee_id": self.employee_id,
            "request_date": self.request_date,
            "overtime_date": self.overtime_date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "num_hour": self.num_hour,
            "hour_type": self.hour_type,
            "reason_type": self.reason_type,
            "remarks": self.remarks,
            "user_id": self.user_id,
            "assign_id": self.assign_id
        }

    @classmethod
    def from_json(cls, json: dict):
        return OvertimeCreateModel(
            employee_id=json['employee_id'],
            request_date=json['request_date'],
            overtime_date=json['overtime_date'],
            start_time=json['start_time'],
            end_time=json['end_time'],
            num_hour=json['num_hour'],
            hour_type=json['hour_type'],
            reason_type=json['reason_type'],
            remarks=json['remarks'],
            user_id=json['user_id'],
            assign_id=json['assign_id']
        )
        
class OvertimeEditModel:
    def __init__(
        self,
        request_id,
        request_date,
        payment_date,
        overtime_date,
        start_time,
        end_time,
        num_hour,
        hour_type,
        reason_type,
        remarks,
        user_id,
        assign_id
    ):
        self.request_id = request_id
        self.request_date = request_date
        self.payment_date = payment_date
        self.overtime_date = overtime_date
        self.start_time = start_time
        self.end_time = end_time
        self.num_hour = num_hour
        self.hour_type = hour_type
        self.reason_type = reason_type
        self.remarks = remarks
        self.user_id = user_id
        self.assign_id = assign_id

    def __str__(self) -> dict:
        return {
            "request_id": self.request_id,
            "request_date": self.request_date,
            "payment_date": self.payment_date,
            "overtime_date": self.overtime_date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "num_hour": self.num_hour,
            "hour_type": self.hour_type,
            "reason_type": self.reason_type,
            "remarks": self.remarks,
            "user_id": self.user_id,
            "assign_id": self.assign_id
        }

    @classmethod
    def from_json(cls, json: dict):
        return OvertimeEditModel(
            request_id=json['request_id'],
            request_date=json['request_date'],
            payment_date=json['payment_date'] if 'payment_date' in json else None,
            overtime_date=json['overtime_date'],
            start_time=json['start_time'],
            end_time=json['end_time'],
            num_hour=json['num_hour'],
            hour_type=json['hour_type'],
            reason_type=json['reason_type'],
            remarks=json['remarks'],
            user_id=json['user_id'],
            assign_id=json['assign_id']
        )

class OvertimeDeleteModel:
    def __init__(
        self,
        request_id
    ):
        self.request_id = request_id

    def __str__(self) -> dict:
        return {
            "request_id": self.request_id
        }

    @classmethod
    def from_json(cls, json: dict):
        return OvertimeDeleteModel(
            request_id=json['request_id']
        )
        
class OvertimeAuthModel:
    def __init__(
        self,
        id,
        request_type,
        request_date,
        request_from,
        request_to,
        request_hour,
        request_status
    ):
        self.id = id
        self.request_type = request_type
        self.request_date = request_date
        self.request_from = request_from
        self.request_to = request_to
        self.request_hour = request_hour
        self.request_status = request_status
        
    def __str__(self) -> dict:
        return {
            "id": self.id,
            "request_type": self.request_type,
            "request_date": self.request_date,
            "request_from": self.request_from,
            "request_to": self.request_to,
            "request_hour": self.request_hour,
            "request_status": self.request_status
        }
    
    @classmethod
    def from_json(cls, json: dict):
        return OvertimeAuthModel(
            id=json['ID'],
            request_type=json['RequestType'],
            request_date=json['RequestDate'],
            request_from=json['RequestFrom'],
            request_to=json['RequestTo'],
            request_hour=json['RequestHour'],
            request_status=json['RequestStatus']
        )
       
class OvertimeApproveModel:
    def __init__(
        self,
        request_id,
        request_date,
        payment_date,
        overtime_date,
        start_date_time,
        end_date_time,
        num_hour,
        hour_type,
        reason_type,
        remarks,
        assign_id,
        user_id
    ):
        self.request_id = request_id
        self.request_date = request_date
        self.payment_date = payment_date
        self.overtime_date = overtime_date
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.num_hour = num_hour
        self.hour_type = hour_type
        self.reason_type = reason_type
        self.remarks = remarks
        self.assign_id = assign_id
        self.user_id = user_id

    def __str__(self) -> dict:
        return {
            "request_id": self.request_id,
            "request_date": self.request_date,
            "payment_date": self.payment_date,
            "overtime_date": self.overtime_date,
            "start_date_time": self.start_date_time,
            "end_date_time": self.end_date_time,
            "num_hour": self.num_hour,
            "hour_type": self.hour_type,
            "reason_type": self.reason_type,
            "remarks": self.remarks,
            "assign_id": self.assign_id,
            "user_id": self.user_id
        }

    @classmethod
    def from_json(cls, json: dict):
        return OvertimeApproveModel(
            request_id=json['request_id'],
            request_date=json['request_date'],
            payment_date=json['payment_date'],
            overtime_date=json['overtime_date'],
            start_date_time=json['start_date_time'],
            end_date_time=json['end_date_time'],
            num_hour=json['num_hour'],
            hour_type=json['hour_type'],
            reason_type=json['reason_type'],
            remarks=json['remarks'],
            assign_id=json['assign_id'],
            user_id=json['user_id']
        )
    
class OvertimeRejectModel:
    def __init__(self, request_id, assign_id):
        self.request_id = request_id
        self.assign_id = assign_id

    def __str__(self) -> dict:
        return {
            "request_id": self.request_id,
            "assign_id": self.assign_id
        }

    @classmethod
    def from_json(cls, json: dict):
        return OvertimeRejectModel(
            request_id=json['request_id'],
            assign_id=json['assign_id']
        )
    