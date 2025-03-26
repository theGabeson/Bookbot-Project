from stats import word_counter
from stats import character_counter
from stats import character_sorter
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    #Getting the text from a file
    path = sys.argv[1]
    text = get_book_text(path)

    #Counting the number of words in the file
    word_count = word_counter(text)

    #Counting the number of characters in each 
    number_of_characters = character_counter(text)
    sorted_characters = character_sorter(number_of_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_characters:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()
