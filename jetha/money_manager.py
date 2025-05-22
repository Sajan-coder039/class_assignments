import json
with open("records.json","r") as file:
    data=json.load(file)
    TOTAL=data["total"]
        
class Money:
    def __init__(self):
        self.total=TOTAL
    
    def deposit(self,amount):
        self.total+=amount
        return f"THE NEW BALLANCE: {self.total}"
    
    def withdraw(self,amount):
        self.total-=amount
        return f"THE NEW BALANCE: {self.total}"
    
    def check_balance(self):
        return f"THE CURRENT BALANCE: {self.total}"




