# Write a program to read a text file and display the count of vowels and consonants in the file

with open("Marks.txt", "r") as file:
    vowels = 0
    consonants = 0
    for line in file:
        for char in line:
            if char.isalpha():
                if char.lower() in "aeiou":
                    vowels += 1
                else:
                    consonants += 1
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")