def get_book_text(path_to_file):
	with open (path_to_file) as f:
		file_contents = f.read()
	return file_contents

def main():
	read_book = get_book_text("books/frankenstein.txt")
	#print(read_book)
	word_number = len(read_book.split())
	print(f"{word_number} words found in the document")