global var1  
global var2  
global var3  
global var4
global var5
var1 = 0
var2 = 0
var3 = 0
var4 = 0
var5 = 0
import time
import utilities
import subprocess

firsttime = 1

# VoltOS Version Goes here #
#--------------------------#
ver = 1.5        
#--------------------------#


Version = float(ver)



class PROGRAMS():





 def randnum():
     from random import seed
     from random import randint
     print("Random Number Game")
     x = 1
     y = 10
     for _ in range(1):
         num = randint(x,y)
     guess = int(input("Guess a number between 1 and 10."))
     if(guess == num):
         print("Your guess was correct!")
     else: 
         print(" Your guess was incorrect.")
         print("The correct guess was " + str(num) + ".")

 

 def edit():
    print("\n")
    print("Text editor 1.0 VoltOS build. Enter quit to stop.")
    i = 1
    while(i == 1):
     x = input(" ")

     if(x == "quit"):
         break

















class OS():

 def __init__():

     var1 = 0 # I know these are unused but these are here if you need them coding memory checks.
     var2 = 0
     var3 = 0
     var4 = 0
     var5 = 0
 def help():
     print("Commands:")
     print("OS.write()")
     print("Syntax: OS.write(variable you want to write to, data you want to write)")
     print("OS.math()")
     print("Syntax: OS.math(operation, + = 1, - = 2, * = 3, / = 4., number a, number b)")
     print("OS.launch()")
     print("Syntax: OS.launch(program to run)")
     print("Programs:")
     print("VIRIDI")
     print("RANDNUM")
     print("CONFIG")
     print("TXTEDIT")
     print("(Only run after using CONFIG.)")
     print("EXTERNAL1")
     print("EXTERNAL2")
     print("EXTERNAL3")
     print("(The rest of these are fine.)")
     print("SETUP")
     print("\n")
 def write(x,y):
     global ans
     if(x == 1):
         global var1
         var1 = y
         print("Suceeded.")
         print(var1)
         return var1
     if(x == 2):
         global var2
         var2 = y
         print("Suceeded.")
         print(var2)
         return var2

     if(x == 3):
         global var3
         var3 = y
         print("Suceeded.")
         print(var3)
         return var3
     if(x == 4):
         global var4
         var4 = y
         print("Suceeded.")
         print(var4)
         return var4
     if(x == 5): 
         global var5
         var5 = y
         print("Suceeded.")
         print(var5)
         return var5

 def math(a,b,c):
     if(a == 1):
         ans = a + b
         print("Suceeded.")
         print(ans)
         return ans
     if(a == 2):
         ans = a - b
         print("Suceeded.")
         print(ans)
         return ans
     if(a == 3):
         ans = a * b
         print("Suceeded.")
         print(ans)
         return ans

     if(a == 4):
         ans = a / b
         print("Suceeded.")
         print(ans)
         return ans

 def launch(program):

     global xyz

     global xyza

     global xyzb

     global xyzc
     if(program == "OTAUPD"):
         pass # to be added soonTM
     if(program == "CHAT"):
         print("|Chat|")
         selection = input("Press 1 to start a server and press 2 to start a client.")
         if(selection == 1):
             print("This will be available in 1.6!")
             
             OS.start()
         elif(selection == 2):
             print("This will be available in 1.6!")
             
             OS.start()
         else:
             print("Invalid selection")
             OS.start()

     if(program == "VIRIDI"):

         subprocess.call("TCG.Game.py", shell=True)

     if(program == "RANDNUM"):

         PROGRAMS.randnum()

     if(program == "CONFIG"):

         qwerty = int(input("Press 1 to configure external file 1, and Press 2 to configure external file 2, and so on with 3."))

         if(qwerty == 1):

             print("Configuring external file 1.")

             xyz = input("Please specify the file name. (filename.py)")

         if(qwerty == 2):

             print("Configuring external file 2.")

             xyza = input("Please specify the file name. (filename.py)")

         if(qwerty == 3):

             print("Configuring external file 3.")

             xyzb = input("Please specify the file name. (filename.py)")        

     if(program == "EXTERNAL1"):

         print("Running external program 1.")

         print("\n")

         subprocess.call(xyz, shell=True)

     if(program == "EXTERNAL2"):

         print("Running external program 2.")

         print("\n")

         subprocess.call(xyza, shell=True)

     if(program == "EXTERNAL3"):

         print("Running external program 3.")

         print("\n")

         subprocess.call(xyzb, shell=True)

     if(program == "TXTEDIT"):

         print("Running Text Editor.")

         print("\n")

         PROGRAMS.edit()

     if(program == "SETUP"):

         print("\n")

         OS.setup()


 def start():

     print("Welcome to VoltOS. V1.5")

     print("\n")

     x = int(input("Press 1 to open launcher. Press 2 to use a write command. Press 3 to use a math command. Press 4 for help. Press 5 to log out."))

     if(x == 1):

         y = input("What program would you like to launch? (Press back to go back.)")

         if(y == "CONFIG"):

             OS.launch("CONFIG")

             OS.start()

         if(y == "MAIL"):

             OS.launch("MAIL")

             OS.start()

         if(y == "VIRIDI"):

             OS.launch("VIRIDI")

             OS.start()

         if(y == "RANDNUM"):

             OS.launch("RANDNUM")

             OS.start()

         if(y == "EXTERNAL1"):

             OS.launch("EXTERNAL1")

             OS.start()

         if(y == "EXTERNAL2"):

             OS.launch("EXTERNAL2")

             OS.start()

         if(y == "EXTERNAL3"):

             OS.launch("EXTERNAL3")

             OS.start()

         if(y == "TXTEDIT"):

             OS.launch("TXTEDIT")

             OS.start()

         if(y == "SETUP"):

             OS.launch("SETUP")

             OS.start()

         if(y == "back"):

             OS.start()

     if(x == 2):

         z = int(input("arg 1 (write location)"))

         a = int(input("arg 2 (write value)"))

         OS.write(z,a)

         OS.start()

     if(x == 3):

         ab = int(input("arg 1 (operation)"))

         abc = int(input("arg 2 (num 1)"))

         n = int(input("arg 3 (num 2)"))

         OS.math(ab,abc,n)

         OS.start()

     if(x == 4):

         OS.help()

         OS.start()

     if(x == 5):

         OS.login()

 def setup():

     global passw

     global firsttime

     print("Setup V1")

     if(firsttime == 1):

         print("It appears this is your first time using VoltOS. Please proceed with setup. Setup V1")

     passw = input("What would you like your password to be? You can change this later by launching SETUP.")

     firsttime = 0

     OS.start()

 def login():

     global passw

     global firsttime

     if(firsttime != 1):

         print("VoltOS Login")

         if(input("Please enter your password.") == passw):

             print("Password Accepted.")

             OS.start()

         else:

             print("Incorrect password. Try again.")

             OS.login()

     else:

         OS.setup()












if __name__ == "__main__":
    OS.login()


