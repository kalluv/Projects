import random

#The user is asked to enter the length of the password.
password_length = int(input("Enter the length of the password:"))

#The letters, numbers and special characters that will be used in the password are stored in a string. 
string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

#A random sample of a length specified by the user, is taken from the string above.
#The random password that will be generated is done by converting the random sample from a list into a string
password = random.sample(string, password_length)

print(password)
