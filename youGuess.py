""" This is a guess number game, enter start to begin,once begin,the 
system workout a random number during 1-1000,then you
have five times to guess the number.when you guess ,system will tell you
your number is bigger or less than the certern number"

"""
import random
def startGame():
    sysnum=random.randint(1,1000)
    print "Ok,we have generate a number please guess"
    choice = raw_input( "enter y to goon ,enter q to quit ")
    if choice == 'y':
       guess(sysnum)
    elif choice == 'q':
       endGame()    
    else :
      print "wrong choice"
      endGame()

def endGame():
     print "The game is over"

def guess(a):   
     print a
     guesscount=1
     while guesscount <=5 :
       print " you %d time to guess"% guesscount
       guessnum = raw_input("enter your number")
       print guessnum
       if a>guessnum:
           print "smaller"
       elif a < guessnum:
           print "bigger"
           print a,guessnum
       else :
           print "congratulation"
           endGame()
#         break
       guesscount = guesscount+1
     endGame() 
startGame()     





