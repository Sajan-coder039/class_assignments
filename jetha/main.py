import os
import json
from datetime import datetime
import time

with open("records.json","r") as file:
    data=json.load(file)
    TOTAL=data["sajan"][0]["total"]
        
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
        return self.total


money=Money()
now=datetime.now().date().isoformat()

while True:
    print(f"date-> {now}")
    user=int(input("Enter the choice:\n 1)check balance \n 2)Deposit money  \n 3)withdraw money \n 4)close my account\n->>"))
    if user==1:
        response=money.check_balance()
        print(f"your current balance is {response}")
        time.sleep(5)
        os.system("clear")
        
    elif user==2:
        amount=int(input("enter the amount: "))
        response=money.deposit(amount)
        print(response)
        dictor={"Date":now,
                "amount": amount,
            "Action":response                
    }   
        data["sajan"].append(dictor)
        with open("records.json", "w") as file:
            json.dump(data,file,indent=4)
        time.sleep(5)
        os.system("clear")
        
    elif user==3:
        amount=int(input("enter the amount: "))
        response=money.withdraw(amount)
        print(response)
        dictor={"Date":now,
                "amount": amount,
            "Action":response                
    }
        data["sajan"].append(dictor)
        with open("records.json", "w") as file:
            json.dump(data,file,indent=4)
        time.sleep(5)
        os.system("clear")
        
    elif user==4:
        print("Thank for you using sajan sir!!")
        break
    
    else:
        print("enter the valid number sir!!")
        time.sleep(3)
        os.system("clear")

    
with open("records.json","r+") as con:
    
    data["sajan"][0]["total"] = money.check_balance()

    con.seek(0)
    json.dump(data, con, indent=4)
    con.truncate()
