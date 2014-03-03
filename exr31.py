print "You enter a dark room with two doors.Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There 's a giant bear here,what do you do ?"
    print "1, Take the cake."
    print "2. scream ate the bear."
    
    bear = raw_input("> ")
    if bear == "1":
    	print "The bear eats your face off, good job!"
    elif bear == "2":
	print "The bear eats your legs off.Good job."
    else :
	print "Well , doing %s is probally better.Bear runs away" % bear
elif door == "2":
    print "You stare into the endless abyss at Cthuhlu's retina."
    print" 1, Blueberries."
    print "2, Yellow jacket clothespins."
    print "3 ,Understaning revolvers yelling melodies."

    insanity = raw_input("> ")
    if insanity == "1" or insanity == "2":
	print "Your body survives"
    else:
	print "The insanity rots your eyes into a pool of muck ."
else:
    print"You stumble around and fall on a knife and die."

