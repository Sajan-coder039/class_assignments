from datetime import datetime,timedelta

while True:
    now=datetime.now().date()+timedelta(days=1)
    task=input("enter your day's task: \n")
    with open("routine.txt","a") as file:
        file.writelines(f"\n{now}\n")
        file.close()
    with open("routine.txt","a") as file:
        file.writelines(task)
        file.close()
    
    choice=input("enter 'n' to exit : ").lower()
    if choice=='n':
        break
    