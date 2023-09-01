#this func to Count no.of words in the file 

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

#this func to Count no.of Lines in the file 

def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

file_path = '/home/mohamedashraf/tes.txt'  

word_count = count_words(file_path)
line_count = count_lines(file_path)

print(f"Number of words: {word_count}")
print(f"Number of lines: {line_count}")
