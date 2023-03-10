from flask_jwt_extended import (jwt_required, 
                                get_jwt, 
                                create_access_token, 
                                create_refresh_token,
                                get_jwt_identity)
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas.user import (UserLoginSchema, 
                          UserSchema, 
                          UserPasswordSchema, 
                          UserMenuSchema,
                          UserLogoutSchema,
                          RefreshTokenSchema)

from conn import conn, myCursor

from models.menu_model import MenuModel
from models.user_model import UserModel

from blocklist import BLOCKLIST

import pandas as pd

blp = Blueprint("User", __name__, description="Operation on users")

@blp.route("/user")
class User(MethodView):
    @jwt_required()
    @blp.response(200, UserSchema)
    @blp.doc(description="Return user informations by ID", summary="Get Logged In User Information")
    def get(self):
        # Get User_ID from JWT
        user_id = get_jwt_identity()
        
        try:
            sql = """
                SET NOCOUNT ON;
                EXEC [dbo].[Account_Fundamentals] 
                    @userid='{user_id}';
                """.format(user_id=user_id)
                
            test = pd.read_sql_query(sql, conn)

        except Exception as err:
            abort(500, message=f"{err}")
        else:
            if not test.to_dict("records"):
                abort(404, message=f"No user with that user_id={user_id}.")
            item = test.to_dict('records')[0]
            data = UserModel.from_json(item)

            return data, 200
        
    @jwt_required()
    @blp.arguments(UserPasswordSchema)
    @blp.response(200, UserPasswordSchema)
    @blp.doc(summary="Update logged in user's password")
    def put(self, user_data):
        user_id = get_jwt_identity()
        try:
            sql = """
            DECLARE @return nvarchar(max) 
            EXEC Account_ChangePassword 
                @UserID=?, 
                @OldPass=?, 
                @NewPass=?, 
                @retval=@return OUTPUT;
            """
            values = (
                user_id,
                user_data['old_password'],
                user_data['new_password']
            )
            myCursor.execute(sql, values)
        except Exception:
            abort(500, message="Invalid credentials")
        else:
            conn.commit()
            return {"message": f"Password updated for User {user_id}."}

@blp.route('/refresh')
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)
    @blp.response(200, RefreshTokenSchema)
    @blp.doc(summary="Refresh logged in user's access_token(not fresh) after it expires.")
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}
        
@blp.route('/user/menu')
class UserMenu(MethodView):
    @jwt_required()
    @blp.response(200, UserMenuSchema(many=True))
    @blp.doc(summary="Get logged in user menus (Mobile)")
    def get(self):
        # Getting User_ID from JWT
        user_id = get_jwt_identity() # Equivalent to get_jwt()['sub'] => " sub = id "
        try:
            sql = """
            EXEC [dbo].[Account_MobileMenu] 
                @userid='{user_id}';
            """.format(user_id=user_id)
            query_data = pd.read_sql_query(sql, conn)
        except Exception:
            abort(500, message=f"Error occurred while getting Menus for User({user_id}).")
        else:
            data = []
            for item in query_data.to_dict("records"):
                data.append(MenuModel.from_json(json=item))
            
            return data

@blp.route('/login')
class UserLogin(MethodView):
    @blp.arguments(UserLoginSchema)
    @blp.response(200, UserLoginSchema)
    @blp.doc(summary="Verify user credentials")
    def post(self, user_data):
        try:
            sql = """
            DECLARE @count INT;
                EXEC [dbo].[Account_Login] 
                @UserID=?, 
                @Password=?, 
                @remoteAddr=?, 
                @retval=@count OUTPUT;
            SELECT @count;
            """
            
            values = (
                user_data['username'],
                user_data['password'],
                str(user_data['remote_addr'])
            )
            print(user_data)
            myCursor.execute(sql, values)
        except Exception:
            abort(401, message="Invalid username or password")
        else:
            access_token = create_access_token(identity=user_data['username'], fresh=True)
            refresh_token = create_refresh_token(identity=user_data['username'])
            
            return {
                "message": "Successfully Logged in.",
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 200
            
@blp.route('/logout')
class UserLogout(MethodView):
    @jwt_required(verify_type=False)
    @blp.arguments(UserLogoutSchema)
    @blp.response(200, UserLogoutSchema)
    @blp.doc(
        description="Should sent 2 separate requests from FrontEnd with Header of access_token and refresh_token", 
        summary="Revoke access_token and refresh_token"
    )
    def delete(self, user_data):
        try:
            token = get_jwt()
            user_id = token['sub']
            sql = """
            DECLARE @count INT,@msg nvarchar(50);
            EXEC [dbo].[Account_Logout] 
                @UserID=?, 
                @remoteAddr=?, 
                @retval=@count OUTPUT;
            """
            values = (
                user_id, 
                str(user_data['remote_addr'])
            )
            myCursor.execute(sql, values)
        except Exception:
            abort(500, message="Error occurred while logging out.")
        else:
            jti = token['jti']
            BLOCKLIST.add(jti)
            print(BLOCKLIST)
            return {"message": "Logged out successfully."}, 200