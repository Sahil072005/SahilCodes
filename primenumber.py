num=int(input("enter a number : "))
for i in range(1,num+1):
    if(num%i==0):
        print("number is prime ")
        break
    else:
         print("the number is not prime ")
         break
