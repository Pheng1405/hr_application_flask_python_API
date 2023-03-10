class MenuModel:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __str__(self) -> dict:
        {
            "id": self.id,
            "name": self.name
        }
        
    @classmethod
    def from_json(cls, json: dict):
        return MenuModel(
            id=json['ID'],
            name=json['FuncDesc']
        )