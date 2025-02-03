# Write a program to read a text file line by line and display each word separated by a #
with open("Marks.txt", "r") as file: [print("#".join(line.split())) for line in file]

