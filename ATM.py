#ATM 

correct_name = "Audry Abonyo"
correct_password = 12345
account_balance = 10000

input_name = input("Enter your account name: ")
input_password = int(input("Enter your account password: "))

if input_name == correct_name and input_password == correct_password:
    print(f"Log in successful {correct_name}")
    print(f"Your account balance is: {account_balance}")

elif input_name != correct_name and input_password == correct_password:
    print("Log in failed. Please put correct account name.")

elif input_name == correct_name and input_password != correct_password:
    print("Log in failed. Please put correct account password. ")

else:
    print("Log in failed; account name and password are incorrect")