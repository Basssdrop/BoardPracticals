# Remove all the lines in the file that contains the character 'a' in a file and write it to another file.
with open("file1.txt", 'r') as f:
    lines = f.readlines()

with open("file1.txt", 'w') as f1, open("file.txt", 'w') as f2:
    for line in lines:
        if 'a' not in line:
            f1.write(line)
        else:
            f2.write(line)