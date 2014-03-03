from random import randint

class level1(object):
    def __init__(self):
	#receive the answer result,if result = 1 ,answer is right,else answer is wrong
        self.level = 1
    	self.right_wrong = 1

    def choose_problem(self):
	print "First ,Welcom to the game!"
        result = "problem"+str(randint(1,1))
	self.right_wrong = result()
        # return the result of this level
	return self.right_wrong

    def problem1(self,level):
	print "Question:What's 2 +3 *3 is ?"
	count =3
	while count < 1:
	     count -= 1
	     result = raw_input()
       	     if int(result) == 11:
		print "you pass the level 1"
             	return 1
	     else:
 	     	print "The wrong,you have %d times to answer" % count

        print "Sorry ,you faild"
        return 0



