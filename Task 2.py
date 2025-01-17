import random
import string

def passwordgenerator(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for i in range(length))
    return password

length=int(input("Enter the Length of the password : "))
password=passwordgenerator(length)
print("Password : ",password)