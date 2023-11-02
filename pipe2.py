# Open the file in read mode
file_path = ''
mixed_word_list = []

try:
    with open(file_path, 'r') as file:
        # Read each line from the file
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace and newline characters

            # Check if the line contains '|' to determine if it's a pair of words
            if '|' in line:
                words = line.split('|')  # Split the line by '|'
                if len(words) == 2:
                    mixed_word_list.extend([word.strip() for word in words])
                else:
                    print(f"Ignoring line: {line} (Expected format: word1 | word2)")
            else:
                mixed_word_list.append(line)
except FileNotFoundError:
    print("File not found.")

# Print the mixed list of words
print(mixed_word_list)