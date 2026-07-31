#input output and type conversion 
#output - print ()

#user input
name = input("Enter your name: ")
print("What's up" + name)

#strings
#f stings - easier to read , no need to conert data types manualy , can include operators

age = input("when were you born")
print(2026-int(age))
print(f"you are {2026-int(age)} years old") #using f string 

height = input("whats your height in meters")
print(f"your height is {height}meters")

#errors 
age = int(input("when were you born?"))
print((age)+10)

#type conversion 
#changing the value from one data type to another

age = 20
print(float(age))

#strings and indexing
county = "Nairobi"
print(county[0])
print(county[1])
print(county[-1])
print(county[:4])
print(county[:-4])

name = "Audry Abonyo"
print(name.upper())
print(name.lower())
print(name.split())
print(name.replace("Audry","Aluoch"))
print(name.strip())

#join
  #joins a list into one string