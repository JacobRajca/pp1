import MyText as mytext

new_string = 'An apple a day keeps the doctor away'
x = mytext.num_word(new_string)
y = mytext.sort_arr(new_string)
z = mytext.alpha_arr(new_string)
print(f'Text: {new_string}')
print(f'Number of words: {x}')
print(f'Words from the longest: {y}')
print(f'Words ordered alphabetically: {z}')