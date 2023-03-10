class UserModel:
    def __init__(self,
                 company_id,
                 branch_id,
                 user_id,
                 user_password,
                 user_first_name,
                 user_last_name,
                 user_sl_name,
                 user_description):
        
        self.company_id = company_id
        self.branch_id = branch_id
        self.user_id = user_id
        self.user_password = user_password
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_sl_name = user_sl_name
        self.user_description = user_description
    
    def __str__(self) -> dict:
        {
            "company_id": self.company_id,
            "branch_id": self.branch_id,
            "user_id": self.user_id,
            "user_password": self.user_password,
            "user_first_name": self.user_first_name,
            "user_last_name": self.user_last_name,
            "user_sl_name": self.user_sl_name,
            "user_description": self.user_description
        }
        
    @classmethod
    def from_json(cls, json: dict):
        return UserModel(
            company_id=json["CompanyID"],
            branch_id=json["BranchID"],
            user_id=json["UserID"],
            user_password=json["UserPWD"],
            user_first_name=json["UFName"],
            user_last_name=json["ULName"],
            user_sl_name=json["USLName"],
            user_description=json["UDesc"]
        )
        