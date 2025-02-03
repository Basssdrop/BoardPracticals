# Write a program to read a text file and display the count of vowels and consonants in the file
vowels, consonants = sum(char.lower() in "aeiou" for line in open("Marks.txt") for char in line if char.isalpha()), sum(char.lower() not in "aeiou" for line in open("Marks.txt") for char in line if char.isalpha())
