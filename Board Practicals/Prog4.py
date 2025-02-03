# Create a binary file with name and roll no. Then Seach for a given roll no. and display the name, if not found display appropriate message

import pickle
f1 = open("1.pkl", "wb")
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter the name: ")
    roll = input("Enter the roll number: ")
    pickle.dump((name, roll), f1)
f1.close()
f2 = open("1.pkl", "rb")
roll = input("Enter the roll number to search: ")
found = False
try:
    while True:
        name, r = pickle.load(f2)
        if r == roll:
            print(f"Name: {name}")
            found = True
            break
except EOFError:
    if not found:
        print("Roll number not found")
f2.close()