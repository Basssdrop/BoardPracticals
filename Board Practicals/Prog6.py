# Write a function that reads a csv fil and creates another csv file with the same content, but with a different delimiter.

def change_delimiter(input_file, output_file, old_delimiter, new_delimiter):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f1:
        for line in lines:
            f1.write(line.replace(old_delimiter, new_delimiter))

change_delimiter("employee.csv", "copyemployee.csv", ',', '|')