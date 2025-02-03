# Write a program to get roll numbers, names and marks of the students of a class and store these details in a file called Marks.txt

head_count = int(input("Enter the number of students: "))
with open("Marks.txt", "w") as file:
    for i in range(head_count):
        roll = input("Enter the roll number: ")
        name = input("Enter the name: ")
        marks = input("Enter the marks: ")
        file.write(f"{roll} {name} {marks}\n")