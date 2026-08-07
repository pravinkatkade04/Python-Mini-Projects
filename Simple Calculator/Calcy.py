a = int(input("\n Enter First Number :- "))
b = int(input(" \n Enter Second Number :- "))



print("\n Please Enter , What you Want to perform ADD,SUB,MUL,DIV \n ")
print("Press : \n 1 for Addition \n 2 for Substraction \n 3 for Multiplication \n 4 for Division\n ")

ip = input()


if ip == "1":
    print("Addition of " , a ,"&" , b ,"is :" , a+b)
elif ip == "2":
    print("Substraction of " , a ,"&" , b ,"is :" , a-b)
elif ip == "3":
    print("Multiplication of " , a ,"&" , b ,"is :" , a*b)
elif ip == "4":
    print("Division of " , a ,"&" , b ,"is :" , a/b)
else:
    print("\n Oops... , You Entered Number Is Invalid , Please TRY AGAIN ! ")
