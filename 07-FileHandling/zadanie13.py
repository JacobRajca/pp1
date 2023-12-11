movie_titles = ['Shrek', 'Shrek2', 'Shrek3','Shrek Forever','Deadpool']

file = open('movies.txt','w')
for element in movie_titles:
    file.write(element+'\n')
file.close()