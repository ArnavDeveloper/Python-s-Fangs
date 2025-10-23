#listed all food items in store
Food=["Burger" , "Pizza" , "Chilli Paneer" , "Momos"]
#All necessary variables initialised
Bought=[ ]
Price=[120.50 , 100.75 , 70.20 , 45.00]
Quantity=[ ]
total=0.0

#While loop to take the type of food item and its quantity
while True:
    choice =(input("Enter the food you want to buy from these (Burger , Pizza , Chilli Paneer , Momos) (q to quit)  : "))
    if choice.lower( ) =="q":
          break
    elif choice.title( ) in Food:
           Bought.append(choice)
           qty=int(input("Enter quantity of item you would like to buy:"))
           Quantity.append(qty)
    else:
           print("Not a valid choice(Try again)")
# for loop to find the Bought items in list Food and  calculate total       
for i in range(0,len(Bought)):
    for j in  range(0,len(Food)):
        if Bought[i].lower()== Food[j].lower():
            total+= Quantity[i]*Price[j]
 #Finally total output is given      
print(f"Your Cart items are :{Bought}")
print(f"Your total amount is : {total}")