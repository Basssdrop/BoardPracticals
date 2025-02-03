# Write a program to read a text file line by line and display each word separated by a #

with open("Marks.txt", "r") as file:
    for line in file:
        words = line.split()
        print("#".join(words))
