from sys import exit
from random import randint

def death():
    quips = ["You died. You kinda suck at this.","Nice job, you died...jakass.","Such a luser","I have a small puppy tha's better at this."]
    print quips[randint(0,len(quips)-1)]
    exit(1)

def central_corridor():
    print "The Gothons of the Planet percal# 25 have invaded your ship and destrooyed"
    print "your entire crew. You are the last surviving member and your last"
    print "MISSION"

    action = raw_input("> ")
    if action == "shoot!":
	print "Your dead"
	return 'death'
    elif action == "dodge!":
	print "your head and eats you"
	return 'death'
    elif action == "tell a joke":
	print "Lucky for you "
  	return 'laser_weapon_armory'

    else:
	print "DOES NOT COMPUTE!"
	return 'central_corridor'

def laser_weapon_armory():
    print"You do a dive and you need the code to get the bomb"
    print "wrong 10 time then the lock closes forever and you can't leave"
    code ="%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
    guess = raw_input("> ")
    guesses = 0
    
    while guess != code and guesses <10 and guess != "000000":
	print "BZZZZEDDD!"
	guesses += 1
 	guess = raw_input(" > ")

    if guess == code or guess == "000000":
	print "Your guess the code"
	return 'the_bridge'

    else:
	print "you are dead"
	return 'death'

def the_bridge():
    print "you burst onto the bridge"
    action = raw_input(".>")
    
    if action == "throw the bomb":
 	print"it goes off."
        return 'death'

    elif action =="slowly place the bomb":
	print "get off this thin can."
	return 'escape_pod'
    else:
	print "DOES NOT COMPUTE"
	return "the_bridge"

def escape_pod():
    print "do you take?"
    
    good_pod = randint(1,5)
    guess = raw_input("[pdd 1-5]>")

    if int(guess) != good_pod:
	print "You jump into pod %s and hit the eject button" % guess
        return 'death'

    else:
    	print "time . You won"
	exit(0)

ROOMS = {'death':death,'central_corridor':central_corridor,
         'laser_weapon_armory': laser_weapon_armory,
 	 'the_bridge': the_bridge,
	 'escape_pod': escape_pod
	}

def runner(map,start):
    next = start
    while True:
	room = map[next]
	print "\n -------------"
	next = room()

runner(ROOMS,'central_corridor')
 	
	    
