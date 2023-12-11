def num_word(text):
    i = 0
    words = 0
    while i < len(text):
        if text[i] == ' ':
            words +=1
        i+=1
    return words+1

def sort_arr(text):
    arr = text.split()
    return sorted(arr,key=len,reverse=True)

def alpha_arr(text):
    arr = text.split()
    return sorted(arr)