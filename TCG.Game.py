from random import seed
from random import randint

#invis data on what cards are obtained. might be used in future
def library():
    global cards
    cards = []
library()
def opencards():
 seed(randint(1,386029149)) 
 for _ in range(1):
   card = randint(1,9)
 if(card == 1):
     print(" _________")
     print("|idiot|120|")
     print("|    \o/  |")
     print("|     |   |")
     print("|____/_\__|")
     print("|punch  90|")
     print("|     UC,S|")
     print("|_________|")
     print("Uncommon, Strong ID.1")
     cards.append(1)
 if(card == 2):
     print(" _________")
     print("|idiot|80 |")
     print("|    \o/  |")
     print("|     |   |")
     print("|____/_\__|")
     print("|punch  30|")
     print("|      C,W|")
     print("|_________|")
     print("Common, Weak  ID.2")
     cards.append(2)
 if(card == 3):
     print(" _________")
     print("|sword|C,I|")
     print("|=E+====> |")
     print("|_________|")
     print("|this can |")
     print("|increase |")
     print("|dmg +20. |")
     print("|_________|")
     print("Common Item ID.3")
     cards.append(3)
 if(card == 4):
     print(" _________")
     print("|knight|40|")
     print("|  \D p->  |")
     print("|   0/    |")
     print("|__/_\____|")
     print("|stab  70 |")
     print("|     UC,W|")
     print("|_________|")
     print("Uncommon, Weak ID.4")
     cards.append(4)
 if(card == 5):
     print(" _________")
     print("|bomb|  10|")
     print("|     /   |")
     print("|    /_\  |")
     print("|____\_/__|")
     print("|boom  300|")
     print("|     R,GC|")
     print("|_________|")
     print("Rare, Glass Cannon ID.5")
     print("Note: uses 'boom' on death")
     cards.append(5)
 if(card == 6):
     print(" _________")
     print("|Pill|UC,I|")
     print("|  __ Rx  |")
     print("| (_|)    |")
     print("|         |")
     print("|heals 50 |")
     print("|when used|")
     print("|_________|")
     print("Uncommon, Item ID.6")
     cards.append(6)
 if(card == 7):
     print(" _________")
     print("|Bee|  20 |")
     print("|  __ Rx  |")
     print("|+(| | |)o|")
     print("|   U     |")
     print("|sting  50|")
     print("|      C,W|")
     print("|_________|")
     print("Common, Weak ID.7")
     cards.append(7)
 if(card == 8):
     print(" _________")
     print("|rock|UC,I|")
     print("|  __     |")
     print("| (__)    |")
     print("|         |")
     print("|heals 20 |")
     print("|when used|")
     print("|_________|")
     print("Uncommon, Item ID.8")
     cards.append(8)
 if(card == 9):
     print(" __________________________________________________")
     print("|PROMOCARD            woo                          |")
     print("|                 \o/                              |")
     print("|                  |                               |")
     print("|                 / \                              |")
     print("|Go to:                                            |")
     print("|https://virtual-idiots-webpage--killaship.repl.co/|")
     print("|__________________________________________________|")
     print("Rare, Promo ID.P")
     cards.append("P")






def openpack():
 print("You have opened a pack of cards.")
 print("Your 4 cards are:")
 opencards()
 opencards()
 opencards()
 opencards()
 #just here for the IDs so I can look at the cards without looking at them.
 for x in range(len(cards)):
     print(cards[x])

 




print("Welcome to Virtual Idiots!") 
openpack()
