first_name = "Audry"
last_name = "Abonyo"
age = 21
height = 165
weight = 55
university = "Jomo Kengeya University of Agriculture and Technology"
course = "Computer Science"

def myfunc():
    global course
    course = "Information Technology"
    
myfunc()
print("FIRST_NAME : ", first_name)
print("LAST_NAME : ", last_name)
print("AGE : ", age)
print("HEIGHT : ", height)
print("WEIGHT : ", weight)
print("UNIVERSITY : ", university)
print("COURSE : ", course)