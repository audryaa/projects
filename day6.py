#DAY
#decision making 

#comparison operators
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

#if statement
#if condition:
    #do something

age=12
if age >= 18:
    print("you can vote")
    #if...else statemeny
else:
    print("You cannot vote")

#if .....elif .... else statement
score = 90

if score >= 90:
    print("A")

elif score >= 80:
    print("B")

elif score >= 70:
    print("C")
    
else:
    print("FAIL")


#logical operators
#and
#or
#not

age = 20
is_available = False

if age >= 18 and is_available:
    print("You can vote")

else:
    print("You cannot vote")

#or
if age >= 18 or is_available:
    print("You can vote")

else:
    print("You cannot vote")

#not
if not is_available:
    print("You cannot vote")

else:
    print("You can vote")
