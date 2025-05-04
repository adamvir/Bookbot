import sys
from stats import book_word_count, book_ch_count, list_ch_count

def main():
    file_path = input("📚Drop here the book name to count📚: ")
    file_path = f"books/{file_path}.txt"
    num_words = book_word_count(file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print("✅ File loaded successfully.")
    
    except Exception as e:
        print(f"❌ Error: {e}")

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")       
    print("--------- Character Count -------")
    list_ch_count(file_path)
    print("============= END ===============")

    
    
    # if len(sys.argv) < 2:
    #     print("Usage: python3 main.py <path_to_book>")
    #     sys.exit(1)

    # else:
    #     file_path = sys.argv[1]
    #     num_words = book_word_count(file_path)
    #     print("============ BOOKBOT ============")
    #     print(f"Analyzing book found at {file_path}...")
    #     print("----------- Word Count ----------")
    #     print(f"Found {num_words} total words")
    #     print("--------- Character Count -------")
    #     list_ch_count(file_path)
    #     print("============= END ===============")
    #     sys.exit(0)
main()
                   
        



    





 