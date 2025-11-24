import sys
from stats import get_count_words, char_appears_count, get_sorted_list

def get_book_text(filepath):

    with open(filepath) as f:
        contents = f.read()

    return contents


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


bookpath = sys.argv[1] #"books/frankenstein.txt"
text_string = get_book_text(bookpath)
letter_count = get_sorted_list(char_appears_count(text_string))

print("============ BOOKBOT ============")
print(F"Analyzing book found at {bookpath}")
print("----------- Word Count ----------")
print(f"Found {get_count_words(text_string)} total words")
print("--------- Character Count -------")
for dict in letter_count:
    if(dict["name"].isalpha()):
        print(f"{dict["name"]}: {dict["num"]}")