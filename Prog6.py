# Write a function that reads a csv fil and creates another csv file with the same content, but with a different delimiter.
import csv; change_delimiter = lambda input_file, output_file, old_delimiter, new_delimiter: open(output_file, 'w').writelines([line.replace(old_delimiter, new_delimiter) for line in open(input_file, 'r').readlines()])
