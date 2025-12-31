
roll = input("Enter Roll Number: ")
name = input("Enter Name: ")
age = input("Enter Age: ")
with open("student.txt","w") as f:
    f.write(f"Roll Number: {roll}\nName: {name}\nAge: {age}")
