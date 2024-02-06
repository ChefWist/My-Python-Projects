print("Sign Up:")

username = input("Username: ")
password = input("Password: ")

login_details = [username,password]
print("Signed Up!")

username = ""
password = ""
print(" ")

while not(username == login_details[0] and password == login_details[1]):
    print("Login:")
    username = input("Username: ")
    password = input("Password: ")
    if not(username == login_details[0] and password == login_details[1]):
        print("Username or Password wrong!")
print("Logged In!")