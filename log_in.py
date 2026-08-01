#LOG IN SYSTEM
username = "THURSDAY"
password = "90DAYS"

while True:
    entered_username = input("Enter your correct username: ")
    entered_password = input("Enter your correct password: ")

    if entered_username == username and entered_password == password:
        print("Log in successful!")
        break #stops the loop if the login is successful
    else:
        print("Invalid username or password. Please try again.")