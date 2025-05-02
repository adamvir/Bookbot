def book_word_count(file_path):
    
    with open(file_path, "r") as f:
        word_count = 0
        file_contents = f.read()
        for word in file_contents.split():
            word_count += 1
    
    return word_count

def book_ch_count(file_path):
    
    with open(file_path, "r") as f:
        ch_count = 0
        dic_count_ch_int = {}
        file_contents = list(f.read().lower())
        
     
        for ch in file_contents:
            if ch in dic_count_ch_int:
                dic_count_ch_int[ch] += 1
            else:
                dic_count_ch_int[ch] = 1
        
    
    return dic_count_ch_int










