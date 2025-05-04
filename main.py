import sys
from stats import book_word_count, book_ch_count, list_ch_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        file_path = sys.argv[1]
        num_words = book_word_count(file_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        list_ch_count(file_path)
        print("============= END ===============")
        sys.exit(0)
main()
                   
        



    





 