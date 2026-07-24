name = input("Enter your name: ")
database_marks = int(input("Enter your Database marks: "))
calculus_marks = int(input("Enter your Calculus marks: "))
programming_marks = int(input("Enter your Programming marks:"))
accounting_marks = int(input("Enter your Accounting marks:"))

total_marks = database_marks + calculus_marks + programming_marks + accounting_marks

average_marks = total_marks / 4

print(f"Student Name: {name} ")
print(f"Database Marks: {database_marks}")
print(f"Calculus Marks: {calculus_marks}")
print(f"Programming Marks: {programming_marks}")
print(f"Accounting Marks: {accounting_marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")

if (database_marks < 0 or database_marks > 100 or calculus_marks < 0 or
     calculus_marks > 100 or programming_marks < 0 or programming_marks > 100
     or accounting_marks < 0 or accounting_marks > 100):
    print("Invalid marks entered")

elif average_marks >= 80:
    print("You scored an A")
    print("Well done!")

elif average_marks >= 60:
    print("You have scored a B")
    print("Good work!")

elif average_marks >= 40:
    print("You have scored a C")
    print("Good attempt!")

else:
    print("You have scored a F")
    print("Please put more effort!")

