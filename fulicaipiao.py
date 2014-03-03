""" This program is to generate a radom number set of fulicaipiao"""

# First create a number set include 22 numbers
import random
numbers = []
def createNumbers():
     i = 1
     while i < 34:
          numbers.append(i)
          i = i +1
       

def getNum():
    size = len(numbers)
    count =random.randint(0,size-1)
    number = numbers[count]
    numbers.remove(number)
    return number

results=[]

def getRedNums():
    j = 1
    while j<= 6:
        result= getNum()
        print "the %d number is %s" %(j,result)
        results.append(result)
        j = j+1

def getBlueNum():
    result=random.randint(1,16)
    results.append(result)
    print "the  blue number is %s" % result

createNumbers()    
getRedNums()
getBlueNum()
 
for i in results:
    print i
    

 
