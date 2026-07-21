print ("Hello world")
print ("My name is Audry Abonyo")


# comment

print ("what is your name? ")

input

# data types
#python data types 
#123 integers 
#nairobi string
#3.12 float
#true boolean 

age = 21

#boolean 
its_raining = True
its_hot = False

print (its_raining)
print (its_hot)
# when writing variables do not enclose them in the speech marks 

print ("My name is Audry an i am" , age , "years old")
print (f"My name is Audry and i am {age}")
# f means a formated string allows you to insert variables directly using a calibracket
print("My name is Audry " + str(21) + "years old")

#type functions 
year = 2019
university = "Jomo kenyatta university of agriculture and technology"
year = 1998

print (type(year))
print (type(university))

#global variables - you can change your data type
x = "Nairobi"

def myfunc():
    global x
    x = "Mombasa"
    
myfunc()
print("I live in",x)