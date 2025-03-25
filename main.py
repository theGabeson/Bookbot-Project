from stats import word_counter
from stats import character_counter

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    #Getting the text from a file
    text = get_book_text("books/frankenstein.txt")
    #Counting the number of words in the file
    word_count = word_counter(text)
    print(f"{word_count} words found in the document")
    #counting the number of characters in each 
    number_of_characters = character_counter(text)
    print(number_of_characters)
    

main()
