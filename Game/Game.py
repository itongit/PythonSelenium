from level1 import *
class Game(object):
    def __init__(self):
	#The score of the game
	self.score = 0
	# The level of the game
	self.level = 0
     	#self.start = start

    #start game 
    def start_game(self):
 	level = self.level


    
    def choose_level(self,current_level,current_score):
 	level = current_level
        score = current_score
        level_name = "level"+str(self.level)
        choose_problem(level)
        
    def pause_game(self):
	print "Are you sure to quit ?"
	result = raw_input("> ")
	if result != "y":
	    print "OK, you will go on !"
            
        else :
	    print "you will quit"
            exit(0)

    def win_game(self):
	print "Congratulation! you have passed all the rooms "
        print "You win"
        exit(1)


    def level_result(self,result):
	result = chooes_problem()
        # reslt = 1,answer is right,goon 
	if result == 1:
	    self.level += 1
	    self.score += 50
	    print "your score is %d " % self.score
            print "enter y to enter next level,q to end game !"
            next_level == raw_input("[level choose y or q")
            if next_level == "y":
		choose_level(self.level,self.score)

	    elif next_level == "q":
		end_game()
	    else:
		print "wrong choice"
                end_game()
	    
          
	elif result == 0:
	    print "restart or quit "
	    choose = raw_input("r to restart q to quit")
            if choose == "r":
                choose_level(self.level,self.score)
            else:
                end_game()

    def end_game(self):
	exit(0)

a_game=Game()
a_game.choose_level(1,1)
