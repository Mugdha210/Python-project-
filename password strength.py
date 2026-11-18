

print("PASSWORD STRENGTH CHECKER")

password = input("Enter your password: ")

if len(password) < 8:

    print("Weak Password")
    print("Password should contain at least 8 characters.")

elif (password.islower() or password.isupper()):

    print("Medium Password")
    print("Try using both uppercase and lowercase letters.")

elif password.isalpha():

    print("Medium Password")
    print("Try adding numbers to your password.")

else:

    print("Strong Password")
