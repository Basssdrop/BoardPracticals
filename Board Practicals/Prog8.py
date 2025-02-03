def reverse_and_double(text):
    stack = list(text)
    reversed_doubled_text = ""
    
    while stack:
        char = stack.pop()
        reversed_doubled_text += char * 2
    
    return reversed_doubled_text

if __name__ == "__main__":
    input_text = input("Enter a line of text: ")
    result = reverse_and_double(input_text)
    print("Output:", result)