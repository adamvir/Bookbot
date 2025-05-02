from stats import book_word_count, book_ch_count

def main():
    file_path = "/Users/viragadam/desktop/bootdev/bookbot/books/frankenstein.txt"
    
    num_words = book_word_count(file_path)
    ch_count =  book_ch_count(file_path)

    print(f"{num_words} words found in the document")
    print(ch_count)

main()





    





 