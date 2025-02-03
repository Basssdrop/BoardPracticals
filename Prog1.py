# Write a program to get roll numbers, names and marks of the students of a class and store these details in a file called Marks.txt
import sys; sys.stdout = open("Marks.txt", "w"); [sys.stdout.write(f"{input('Enter the roll number: ')} {input('Enter the name: ')} {input('Enter the marks: ')}\n") for _ in range(int(input("Enter the number of students: ")))]
