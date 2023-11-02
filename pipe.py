# Open the file in read mode
file_path = ''
word_pairs = []
flattened_word_list = []

try:
    with open(file_path, 'r') as file:
        # Read each line from the file
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace and newline characters
            words = line.split('|')  # Split the line by '|'

            # Ensure there are exactly 2 words in the line
            if len(words) == 2:
                flattened_word_list.extend([word.strip() for word in words])
            else:
                print(f"Ignoring line: {line} (Expected format: word1 | word2)")
except FileNotFoundError:
    print("File not found.")

# Print the flattened list of words
print(flattened_word_list)