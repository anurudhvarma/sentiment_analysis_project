# Open the file in read mode
file_path = ''
word_list = []

try:
    with open(file_path, 'r') as file:
        # Read each line (word) from the file and add it to the list
        for line in file:
            word = line.strip()  # Remove leading/trailing whitespace and newline characters
            word_list.append(word)
except FileNotFoundError:
    print("File not found.")

# Print the list of words
print(word_list)
