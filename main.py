def get_book_text(file_path):
    
    with open(file_path, "r") as f:
    
        file_contents = f.read()

    return file_contents

def word_count(text):
    word_count = 0
    for word in text.split():
        word_count += 1
    
    return word_count



def main():
    file_path = "/Users/viragadam/desktop/bootdev/bookbot/books/frankenstein.txt"
    
    num_words = word_count(get_book_text(file_path))

    print(f"{num_words} words found in the document")

main()





    





 