#a simple Q&A game that gives the score and % mark attained

print('Welcome to my Q & A game.')

prompt = input('Do you want to play? ')
if prompt.lower() != 'yes':
    print('Too bad! Thank You')
    quit()
else:
    print('Good, Game on!.')

score = 0

Question1 = input('What does FAO stand for? ')
if Question1.lower() == 'food and agriculture organisation':
    print('Correct!')
    score += 1
else: 
    print('Wrong')

Question2 = input('What is the opposite of Male? ')
if Question2.lower() == 'female':
    print('Correct!')
    score += 1
else: 
    print('Wrong')


Question3 = input('Solve for x; 2x-1=5. x=?? ')
if Question3 == '2':
    print('Correct!')
    score += 1
else: 
    print('Wrong')

Question4 = input('Find y; 3y+2=-4. y=?? ')
if Question4 == '2':
    print('Correct!')
    score += 1
else: 
    print('Wrong')

Question5 = input('What does UN stand for? ')
if Question5.lower() == 'united nations':
    print('Correct!')
    score += 1
else: 
    print('Wrong')

Question6 = input('How many books are in the bible? ')
if Question6 == '66':
    print('Correct!')
    score += 1
else: 
    print('Wrong') 

Question7 = input('If 9a-1=-4. find a: a= ')
if Question7 == '-1/3':
    print('Correct!')
    score += 1
else: 
    print('Wrong')

Question8 = input("What is the country code for Ethiopia?  ")
if Question8 == '+251':
    print('Correct!')
    score += 1
else: 
    print('Wrong')


print('CONGRATULATIONS!! You got ' + str(score) + ' answers correct a '  + str((score)/8 * 100) + '% MARK')