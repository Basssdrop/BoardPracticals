# Remove all the lines in the file that contains the character 'a' in a file and write it to another file.
lines = [line for line in open("file1.txt", 'r') if 'a' not in line]
