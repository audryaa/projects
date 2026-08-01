#GRADE CALCULATOR
#WRITE A CODE THAT ACCEPTS USER IMPUT ON GRADES SCORED IN A TEST AND THEN YOU WILL OUTPUT THEM AS A, B, C, D, E AND FAIL
# 80-100 = A
# 70-79 = B
# 60-69 = C
# 50-59 = D
# 40-49 = E
# BELOW 40 = FAIL

#LOG IN SYSTEM
#WILL ACCEPT USERNAME AND PASSWORD AND THEN CHECK IF THE USERNAME AND PASSWORD IS CORRECT OR NOT
#IF RIGHT THEN IT WILL PRINT WELCOME AND IF WRONG IT WILL PRINT INVALID USERNAME OR PASSWORD AND TRY AGAIN
#USERNAME = THURSDAY
#PASSWORD = 90DAYS

#MULTIPLICATION TABLE
#WILL ACCEPT A NUMBER FROM THE USER AND THEN PRINT ITS MULTIPLICATION TABLE

#even and odd numbers 1-50 skip multiples of 5 stops at 37
#mini atm

grade = int(input("Enter your grade: "))

if 80 <= grade <= 100:
    print("You scored an A")
elif 70 <= grade <= 79:
    print("You scored a B")
elif 60 <= grade <= 69:
    print("You scored a C")
elif 50 <= grade <= 59:
    print("You scored a D")
elif 40 <= grade <= 49:
    print("You scored an E")
elif grade < 40:
    print("You have failed")
else:
    print("Invalid grade entered")


#LOG IN SYSTEM 

