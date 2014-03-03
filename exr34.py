animals = ['bear', 'tiger', 'pengin', 'zebra', 'monkey']
bear = animals[0]

print "The first animal is at 0 and is a %s " % animals[0]


def find_animal():
    while True :
        number = raw_input("> ")
        number = int(number) 
	if number < 6:
            print "The %d animal is at %d  and is a %s " % (number,number-1, animals[number-1])
	else:
	    print"you chooese a larter number"
 	    break
find_animal()
