import pandas as pd

ip = int(input("\n How Many Task You Want to Add :  "))

list1 = []
date = str(input(" Enter Date :- "))
list1= [ "Date :- " + date  ]


for i in range(ip):
    
        task = input(f"Enter{i+1}th Task :-" )
        list1.append(task)

df = pd.DataFrame({
        "task":list1
})

print(" \n Your Todays Tasks \n ")
for j in list1 :
            print("\t "  , j)

df.to_csv("To_Do_List.csv" , index= False)

print("\n Files saved Successfully \n")

for i in range(3):
        print("\n")

