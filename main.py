from stats import get_num_words, get_num_chars, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()

    return book

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    book = get_book_text(file)
    num_words = get_num_words(book)
    num_chars = get_num_chars(book)
    sorted_chars = sort_dict(num_chars)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print(f"============= END ===============")

main()