from marshmallow import Schema, fields

class PayslipSchema(Schema):
    id = fields.Int(required=True, dump_only=True)
    period_id = fields.Str(required=True, dump_only=True)
    for_month = fields.Str(required=True, dump_only=True)
    program = fields.Str(required=True, dump_only=True)
    position = fields.Str(required=True, dump_only=True)
    child = fields.Int(required=True, dump_only=True)
    spouse = fields.Int(required=True, dump_only=True)
    wage = fields.Float(required=True, dump_only=True)
    addition = fields.Float(required=True, dump_only=True)
    deduction = fields.Float(required=True, dump_only=True)
    gross_salary = fields.Float(required=True, dump_only=True)
    taxable_salary = fields.Float(required=True, dump_only=True)
    tax = fields.Float(required=True, dump_only=True)
    net_salary = fields.Float(required=True, dump_only=True)
    notes = fields.Str(required=True, dump_only=True, allow_none=True)


# class PayslipDashboardSchema(Schema):
#     period_id = fields.Str(required=True, dump_only=True)
#     net_salary = fields.Float(required=True, dump_only=True)
    