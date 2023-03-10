from marshmallow import Schema, fields

class UserLoginSchema(Schema):
    username = fields.Str(required=True, load_only=True)
    password = fields.Str(required=True, load_only=True)
    remote_addr = fields.IPv4(required=True, load_only=True)
    message = fields.Str(required=True, dump_only=True)
    access_token = fields.Str(required=True, dump_only=True)
    refresh_token = fields.Str(required=True, dump_only=True)
    
class UserLogoutSchema(Schema):
    remote_addr = fields.IPv4(required=True)
    message = fields.Str(required=True, dump_only=True)
    
class UserSchema(Schema):
    company_id = fields.Str(dump_only=True)
    branch_id = fields.Str(dump_only=True)
    user_id = fields.Str(dump_only=True)
    user_password = fields.Str(load_only=True)
    user_first_name = fields.Str(dump_only=True)
    user_last_name = fields.Str(dump_only=True)
    user_sl_name = fields.Str(dump_only=True)
    user_description = fields.Str(dump_only=True)
    
class UserPasswordSchema(Schema):
    old_password = fields.Str(required=True, load_only=True)
    new_password = fields.Str(required=True, load_only=True)
    message = fields.Str(required=True, dump_only=True)
    
class UserMenuSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)
    
class RefreshTokenSchema(Schema):
    access_token = fields.Str(required=True, dump_only=True)
    