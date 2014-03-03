class Animal (object):
    
    def scream(self):
	print"animal scream"

# Dog is a Animal
class Dog(Animal):
    
    def __init__(self,name):
	## dog has a name
	self.name = name
    
    def scream(self):
	print "Dogs scream 'w' 'w' 'w'"
    

## Cat is a animal
class Cat(Animal):
    
    def __init__(self,name):
	## Cat has a name
 	self.name = name

    def scream(self):
	print "Cat scream 'miao miao miao'"


## Person is a object
class Person(object):

    def __init__(self,name):
	## person has a name
	self.name = name

    ## Person has a pet of some kind
 	self.pet = None

## Employee is a Person
class Employee(Person):
    def __init__(self,name,salary):
	## Employee has a name 
	super(Employee,self).__init__(name)
 
    	##Employee has a salary
	self.salary = salary

## Fish is a object
class Fish(object):
    pass

##Samon is a fish
class Salmon(Fish):
    pass

## Halibut is a fish
class Halibut(Fish):
    pass

## any is a Animal

ani = Animal()
ani.scream()
##rover is a Dog
rover = Dog("Rover")
rover.scream()

##stan is a cat
satan = Cat("satan")
satan.scream()

## mary is a person
mary = Person("Mary")

##mary ha s pet called satan
mary.pet = satan

## frank is a employee and salary is 120000
frank = Employee("Frank",120000)

##frank has a pet called rover
frank.pet = rover

##flipper is a fish
flipper = Fish()

##crouse is a salmon
crouse = Salmon()

##harry is a halibut
harry = Halibut()
