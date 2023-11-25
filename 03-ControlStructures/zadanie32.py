question1 = input('Are you interested in computer science? (Y/N): ')
question2 = input('Do you like playing computer games? (Y/N): ')
question3 = input('Do you have an Instagram account? (Y/N): ')

if question1 == 'Y':
    answer1 = True
if question1 == 'N':
    answer1 = False

if question2 == 'Y':
    answer2 = True
if question2 == 'N':
    answer2 = False
    
if question3 == 'Y':
    answer3 = True
if question3 == 'N':
    answer3 = False

if answer1 == True:
    print('Interested in computer science: Yes')
else:
    print('Interested in computer science: No')

if answer2 == True:
    print('Playing computer games: Yes')
else:
    print('Playing computer games: No')
    
if answer3 == True:
    print('Has an Instagram account: Yes')
else:
    print('Has an Instagram account: No')