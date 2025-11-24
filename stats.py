def get_count_words(string):

    count = len(string.split())

    return count

def char_appears_count(string):
    string = string.lower()

    dict = {}    

    for letter in string:
        if letter not in dict:
            dict[letter] = 0

        dict[letter] +=1

    return dict   

def sort_on(items):
    return items["num"]         

def get_sorted_list(dict):
    list = []
    for letter in dict:
        list.append({"name": letter, "num": dict[letter]})
    list.sort(reverse=True, key=sort_on)
   
    return list 