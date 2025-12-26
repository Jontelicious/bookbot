from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list
import sys

def get_book_text(file_path):
    
    with open(file_path) as f:
        file_contents = f.read()
        
        return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    file_contents = get_book_text(path_to_book)

    words = get_num_words(file_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    count = get_chars_dict(file_contents)
    char_list = chars_dict_to_sorted_list(count)

    for entry in char_list:
        char = entry["char"]
        num = entry["num"]

        if not char.isalpha():
            continue

        print(f"{char}: {num}")

    print("============= END ===============")

main()