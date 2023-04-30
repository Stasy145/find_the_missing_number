dict = {'a': 70, 'b': 34, 'c': 900, 'd': 152}

def find_largest_value():  
         
    my_list = sorted(list(dict.values()))
    answer = {k:v for k,v in dict.items() if v >= my_list[-2]}
    return answer.keys()
    
print(find_largest_value())    