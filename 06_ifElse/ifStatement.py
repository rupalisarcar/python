age = int(input("Enter your age: "))

if(age >= 18):
    print("You are eligible to vote.")
elif(age == 17):
    print("You can apply for a voter registration.")
elif(age >= 16):
    print("You can apply for a learner's permit.")
else:
    print("You are not eligible to vote.")
