
import numpy as np

ip = int(input("\n Enter The Weather Temperature :- "))

emoji = [
    "👽","👾" , "🤖","😺","👻","🐵","🐼","🐸","🦥","🦭","🦉","😐"
    ]


if (ip >  45) :
    print("The Temperature is Extremely Hot !",np.random.choice(emoji))
elif (ip >=30 and ip<=45):
    print("The Temperature is Hot ",np.random.choice(emoji)) 
elif (ip >= 20 and ip<=29) :
    print("The Temperature is Moderate",np.random.choice(emoji))
elif (ip >0 and ip<=19) :
    print("The Temperature is Cool",np.random.choice(emoji))
elif (ip<0) :
    print("The Temperature is Extremely cold",np.random.choice(emoji))
else :
    print("Try Again", np.random.choice(emoji))


