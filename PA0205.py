#Correcting login details 
CORRECT_USERNAME ="admin"
CORRECT_PASSWORD ="Python123"

print ("==system login==")

#1. Ask the user to enter the username
entered_username = input("Enter Username: ")

#2. Ask the user to enter the password
entered_password =input("Enter Password: ")

#3.Compare the entered information with the correct details
# Use 'and' to check both username and password
if entered_username == CORRECT_USERNAME and entered_password == CORRECT_PASSWORD:
    print (" Login successful")
else:
    print ("Login unsuccessful. Incorrect username or Password.")    