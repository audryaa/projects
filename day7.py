#loops
#repeat something 

print("Today is on Thursday")
#Print this 100 times 

#types of loops 
#while loops
#for loops 

#while loops 

# while condition:
    #code

cake = 1
while cake <= 9:
    print(cake)
    cake += 2

#infinite loops 
#doesn't end
#cake = 1 
#wile cake <= 9:
    #print(cake)

#for loops
#repeat over a sequence 

for numbers in range (7):
    print(numbers)

for i in range (0,12,2):
        print(i)

for letters in "PYTHON":
     print (letters)

#break
#stops loop immediately

for i in range (1,11):
     if i==6:
          break
print(i)

#continue 
#skips one iteration 

for i in range (1,11):
     if i == 5:
          continue
     print(i)