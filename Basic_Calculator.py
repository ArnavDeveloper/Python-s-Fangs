#First Basic program
# Taking user input
choice=int(input("What ate you going to do? [1.+ / 2.- / 3.x /4.%] : "))
  
  n1=int(input("The first no. :"))
  n2=int(input("The Second no. :"))

# Computing result based on input
if choice == 1:
    result=n1+n2
elif choice ==2:   
    result=n1-n2 
elif choice ==3:   
    result=n1*n2 
elif choice ==4:   
    result=n1/n2 
else:
    print("Invalid choice")
# Printing result
print(f"The result of the operation is {result}")