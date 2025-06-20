from stats import get_number_of_words, number_of_characters, sort_dictionary
from sys import argv,exit

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        book = argv[1]
        print(book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {get_number_of_words(get_book_text(book))} total words")
        print("--------- Character Count -------")
        for key, value in sort_dictionary(number_of_characters(get_book_text(book))):
            if key.isalpha():
                print(f"{key}: {value}")

        print("============= END ===============")

def get_book_text(path_to_file):
    file_contents = ""

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents
main()