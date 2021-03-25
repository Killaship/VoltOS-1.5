from random import randint
xyz = []
def welcome():
    global STOCKprice, money, STOCKowned
    money = 250
    STOCKowned = 0
    STOCKprice = randint(1,10)
    print("Welcome to Stock Simulator.") 
    print("\n")
    print("Manual")
    print("When it asks you how much stock to buy, a negative number is selling.")
    print("A positive number is buying. A zero is waiting and doing nothing.")
    print("If you reach 5,000 dollars, you win.")
    print("\n")
    print("You have " + str(STOCKowned) + " stocks.")
    print("You have $" + str(money) + " money.")
    print("The current price of STOCK is the following: $" + str(STOCKprice))    
    print("\n")
    x = int(input("How many stocks would you like to buy?"))
    buySTOCK(x)
    return STOCKprice
def buySTOCK(quantity):
    global STOCKprice, money, STOCKowned
    STOCKowned = STOCKowned + quantity
    if(money == 0 or money < 0):
        print("You bought too many stocks (Overbought $" + str(abs(money)) + ") and lost the game. Reach $5,000 next time to win.")
        print("You may have also reached 0$. Don't do that.")
        welcome()
    if(money == 5000 or money > 5000):
        print("\n")
        print("You won the game by reaching $5,000! Congratulations.")
        print("\n")
        welcome()
    
    if(quantity < 0):
     if(quantity < STOCKowned or quantity == STOCKowned):
         money = money + STOCKprice * abs(quantity)
         newTick()
     else:
         print("You have too little stocks to sell.")
         newTick()
    else:
     money = money - STOCKprice * quantity
     newTick()
    return money, STOCKowned
def newTick():
    global STOCKprice, money, STOCKowned, xyz
    if(STOCKprice > 21):
     STOCKprice = STOCKprice + randint(-20,20)
    else:
     STOCKprice = STOCKprice + randint(0,15)
    print("You have $" + str(money) + " money.")
    print("You have " + str(STOCKowned) + " stocks.")
    print("The current price of 1 stock is the following: $" + str(STOCKprice)) 
    print("\n")   
    x = int(input("How many stocks would you like to buy?"))
    
   # xyz.append(STOCKprice)
   #for i in range(len(xyz)):
   #  print(xyz[i])
    buySTOCK(x)
    return STOCKprice
welcome()