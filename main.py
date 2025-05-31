import datetime
import pandas as pd

data = []

while True:
    now = datetime.datetime.now().date()
    user_input = float(input("Time you put: "))
    
    data.append({"Timestamp": now, "Input": user_input})
    
    choice = input("Continue? (yes or no): ")
    if choice.lower() == "no":
        break

df = pd.DataFrame(data)

df.to_json("sajan.json")