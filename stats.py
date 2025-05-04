def book_word_count(file_path):
    
    with open(file_path, "r") as f:
        word_count = 0
        file_contents = f.read()
        for word in file_contents.split():
            word_count += 1
    
    return word_count

def book_ch_count(file_path):
    
    with open(file_path, "r") as f:
        
        dic_count_ch_int = {}
        file_contents = f.read().lower()
        
     
        for ch in file_contents:
            
            if ch == " ":
                continue
                
            elif ch in dic_count_ch_int:
                dic_count_ch_int[ch] += 1
            
            else:
                dic_count_ch_int[ch] = 1  
    
    return dic_count_ch_int

def list_ch_count(file_path):

    final_list = []
    dictionary = book_ch_count(file_path)

    new_ch_list = list(dictionary)
    new_ch_val = list(dictionary.values())

    for i in range(0, len(new_ch_list)):
    
         one_line = new_ch_val[i], new_ch_list[i]
         final_list.append(one_line)
        
    final_list = sorted(final_list, reverse=True)
    final_dic = dict(final_list)
    final_dic = {value: key for key, value in final_dic.items()}
    final_list_keys = list(final_dic.items())
    
    
    for key, value in final_list_keys:

        print(f"{key}: {value}")




    
        
    
        
        
    

    
   
    
    




    
    
    











