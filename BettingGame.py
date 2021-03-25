#betting simulator
#bugs: obvious math issues lol, you can only do one round before it bugs out
#to do:
#1. make a system checking if you have enough money to bet.
#2. make a system checking if you have $0, if you do, the game ends.
#3. DONE add a little intro screen with ascii text, maybe splash text.
#4.fix the bugs


from random import seed
from random import randint
global money
money = 100
global wager
wager = 0
global endingmoney
endingmoney = 0

def titlescreen():
 seed(randint(1,386029149)) 
 for _ in range(1):
   splash = randint(1,8)
 if(splash == 1):

   print("BBBB       t   t                SSS                l      t  ")
   print("B   B      t   t  ii           S     ii            l      t          ")
   print("BBBB  eee ttt ttt    nnn  ggg   SSS     mmmm  u  u l  aa ttt ooo rrr")
   print("B   B e e  t   t  ii n  n g g      S ii m m m u  u l a a  t  o o r  ")
   print("BBBB  ee   tt  tt ii n  n ggg  SSSS  ii m m m  uuu l aaa  tt ooo r   ")
   print("                            g                                        ")
   print("                          ggg                       123 lines of code!          ")
   print("\n")
 if(splash == 2):
   print("BBBB       t   t                SSS                l      t  ")
   print("B   B      t   t  ii           S     ii            l      t          ")
   print("BBBB  eee ttt ttt    nnn  ggg   SSS     mmmm  u  u l  aa ttt ooo rrr")
   print("B   B e e  t   t  ii n  n g g      S ii m m m u  u l a a  t  o o r  ")
   print("BBBB  ee   tt  tt ii n  n ggg  SSSS  ii m m m  uuu l aaa  tt ooo r   ")
   print("                            g                                        ")
   print("                          ggg                      Free Kandy!                  ")
   print("\n")

 if(splash == 3):
   print("BBBB       t   t                SSS                l      t  ")
   print("B   B      t   t  ii           S     ii            l      t          ")
   print("BBBB  eee ttt ttt    nnn  ggg   SSS     mmmm  u  u l  aa ttt ooo rrr")
   print("B   B e e  t   t  ii n  n g g      S ii m m m u  u l a a  t  o o r  ")
   print("BBBB  ee   tt  tt ii n  n ggg  SSSS  ii m m m  uuu l aaa  tt ooo r   ")
   print("                            g                                        ")
   print("                          ggg                   Definitely Legal!                     ")
   print("\n")
 if(splash == 4):
   print("BBBB       t   t                SSS                l      t  ")
   print("B   B      t   t  ii           S     ii            l      t          ")
   print("BBBB  eee ttt ttt    nnn  ggg   SSS     mmmm  u  u l  aa ttt ooo rrr")
   print("B   B e e  t   t  ii n  n g g      S ii m m m u  u l a a  t  o o r  ")
   print("BBBB  ee   tt  tt ii n  n ggg  SSSS  ii m m m  uuu l aaa  tt ooo r   ")
   print("                            g                                        ")
   print("BBBB       t   t                SSS                l      t  ")
   print("B   B      t   t  ii           S     ii            l      t          ")
   print("BBBB  eee ttt ttt    nnn  ggg   SSS     mmmm  u  u l  aa ttt ooo rrr")
   print("B   B e e  t   t  ii n  n g g      S ii m m m u  u l a a  t  o o r  ")
   print("BBBB  ee   tt  tt ii n  n ggg  SSSS  ii m m m  uuu l aaa  tt ooo r   ")
   print("                            g                                        ")
   print("                          ggg                   Be 57K In Debt Simulator!                     ")
   print("\n")
 if(splash == 6):
   print("BBBB       t   t                SSS                l      t  ")
   print("B   B      t   t  ii           S     ii            l      t          ")
   print("BBBB  eee ttt ttt    nnn  ggg   SSS     mmmm  u  u l  aa ttt ooo rrr")
   print("B   B e e  t   t  ii n  n g g      S ii m m m u  u l a a  t  o o r  ")
   print("BBBB  ee   tt  tt ii n  n ggg  SSSS  ii m m m  uuu l aaa  tt ooo r   ")
   print("                            g                                        ")
   print("                          ggg                  Made of Bacon!                     ")
   print("\n")
 if(splash == 7):
   print("BBBB       t   t                SSS                l      t  ")
   print("B   B      t   t  ii           S     ii            l      t          ")
   print("BBBB  eee ttt ttt    nnn  ggg   SSS     mmmm  u  u l  aa ttt ooo rrr")
   print("B   B e e  t   t  ii n  n g g      S ii m m m u  u l a a  t  o o r  ")
   print("BBBB  ee   tt  tt ii n  n ggg  SSSS  ii m m m  uuu l aaa  tt ooo r   ")
   print("                            g                                        ")
   print("                          ggg                   Stock Market Simulator died!                     ")
   print("\n")

 if(splash == 8):
   print("BBBB       t   t                SSS                l      t  ")
   print("B   B      t   t  ii           S     ii            l      t          ")
   print("BBBB  eee ttt ttt    nnn  ggg   SSS     mmmm  u  u l  aa ttt ooo rrr")
   print("B   B e e  t   t  ii n  n g g      S ii m m m u  u l a a  t  o o r  ")
   print("BBBB  ee   tt  tt ii n  n ggg  SSSS  ii m m m  uuu l aaa  tt ooo r   ")
   print("                            g                                        ")
   print("                          ggg         If you have a gambling addiction, please call 1-800-522-4700!                   ")
   print("\n")

class betting:
  def __init__():
    global reward
  def process():
      wager = int(input('How much of your money do you wager?'))
      global change
      seed(randint(1,386029149))
      for _ in range(1):
          change = randint(1,2)
      if(change == 1):
         endingmoney = money - wager
         print(":( You lost. Your remaining money is:")
         print(endingmoney)
         betting.process()
      else: 
         endingmoney = money + wager
         print(":) You won! Your remaining money is:")
         print(endingmoney)
         betting.process()
     
titlescreen()
betting.process()