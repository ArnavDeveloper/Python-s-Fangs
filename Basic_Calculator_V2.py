#Imported math package
import math

print("Enter no. and then the functions you would like to perform")
#Took input of the first numbee in result to avoid any conflict on division or multiplication

result=int(input("Enter the first number : "))
#The variable flow is used to check the flow of the while loop
Flow= True
while Flow :
    
    choice=int(input("Enter [1.+ | 2.- | 3.x | 4./] : "))
    while choice >4 or choice <1:
         print("Invalid Choice try again")
         choice=int(input(" Enter [1.+ | 2.- | 3.x | 4./] : "))
    n=int(input("Next no.-:"))
# The choice of Functions determine the operation      
    if choice == 1:
       result+=n
    elif choice ==2:   
       result-=n
    elif choice ==3:   
       result*=n
    else:   
       if n==0:
           print("Division by 0 is not possible")
           continue
       else:
           result/=n
  
    Call=input("Enter Y to continue and N to calculate final result : ")
#To control the Flow of the loop
    if Call.upper() =="Y":
       print(f"Current result={result}")
       Flow=True
    else:
        Flow=False
#To print the final result
print(f"The final result : {result}")           