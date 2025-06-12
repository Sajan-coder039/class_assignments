import calendar
from chempy.util import periodic

# year=2025
# month=6

# print(calendar.month(year,month))

# sentence="sajan sah is the hero of nepla nodoubt"
# def longest(sentence):
#     return len(max(sentence.split(), key=len, default=""))
# print(longest(sentence))
n=int(input("enter number to see the table: "))
print("Atomic No.\tName\t\tSymbol\t\tMass")
for i in range(0,n+1):
    print(i+1,end="\t\t")
    if len(periodic.names[i])>7:
        print(periodic.names[i],end="\t")
    else:
        print(periodic.names[i],end="\t\t")
    print(periodic.symbols[i],end="\t\t")
    print(periodic.relative_atomic_masses[i])



