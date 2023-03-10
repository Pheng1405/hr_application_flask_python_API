class PayslipModel:
    def __init__(
        self,
        id,
        period_id,
        for_month,
        program,
        position,
        child,
        spouse,
        wage,
        addition,
        deduction,
        gross_salary,
        taxable_salary,
        tax,
        net_salary,
        notes
    ):
        self.id = id
        self.period_id = period_id
        self.for_month = for_month
        self.program = program
        self.position = position
        self.child = child
        self.spouse = spouse
        self.wage = wage
        self.addition = addition
        self.deduction = deduction
        self.gross_salary = gross_salary
        self.taxable_salary = taxable_salary
        self.tax = tax
        self.net_salary = net_salary
        self.notes = notes

        
    
    def __str__(self) -> dict:
        return {
            "id": self.id,
            "period_id": self.period_id,
            "for_month": self.for_month,
            "program": self.program,
            "position": self.position,
            "child": self.child,
            "spouse": self.spouse,
            "wage": self.wage,
            "addition": self.addition,
            "deduction": self.deduction,
            "gross_salary": self.gross_salary,
            "taxable_salary": self.taxable_salary,
            "tax": self.tax,
            "net_salary": self.net_salary,
            "notes": self.notes
        }
    
    
    @classmethod
    def from_json(cls, json: dict):
        return PayslipModel(
            id=json['ID'],
            period_id=json['PeriodID'],
            for_month=json['For Month'],
            program=json['Program'],
            position=json['Position'],
            child=json['Child'],
            spouse=json['Spouse'],
            wage=json['Wage'],
            addition=json['Addition'],
            deduction=json['Deduction'],
            gross_salary=json['Gross Salary'],
            taxable_salary=json['Taxable Salary'],
            tax=json['Tax'],
            net_salary=json['Net Salary'],
            notes=json['Notes']
        )
    

# class PayslipDashboardModel:
#     def __init__(
#         self, 
#         period_id,
#         net_salary
#     ):
#         self.period_id = period_id,
#         self.net_salary = net_salary
        
        
#     def __str__(self) -> dict:
#         return{
#             "period_id" : self.period_id,
#             "net_salary" : self.net_salary
#         }
    
#     @classmethod
#     def from_json(cls, json:dict):
#         return PayslipDashboardModel(
#             period_id=json["period_id"],
#             net_salary = json['net_salary']
#         )