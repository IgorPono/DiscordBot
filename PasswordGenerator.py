import random, string
password = ""
print("Enter length of password")
length = int(input())
for x in range (0,length):
    characterType= random.randint(0,2)
    if characterType==0:
        password += random.choice(string.ascii_letters)
    elif characterType==1:
        password += random.choice(string.punctuation)
    else:
        password+= random.choice(string.digits)
print(password)