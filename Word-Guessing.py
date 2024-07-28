import random
word_list = ['tiger','lion','dog','cat','zebra','goat','elephant','beer','fox']
word = random.choice(word_list)

tries=5
dashes = ['_']*len(word)
print(' '.join(dashes))
guessed = False
while tries>0:
    guess = input('Guess a letter or word: ')
    if len(word) == len(guess):
        if word==guess:
            guessed = True
            break
        elif word!=guess:
            tries = tries-1
            print(' '.join(dashes))
            print('Incorrect guess,Left only {}attempts'.format(tries))
    elif len(guess)==1:
        if guess in word:
            print('Correct guess,carry on...')
            indices = [i for i, j in enumerate(word)if guess==j]
            for index in indices:
                dashes[index]=guess
            print(' '.join(dashes))
        elif guess not in word:
            tries-=1
            print(' '.join(dashes))
            print('Incorrect guess,Left only {}attempts'.format(tries))
    else:
        print('Invalid!')
    if word==''.join(dashes):
        guessed=True
        break
if guessed:
    print('You win!')
else:
    print('Game OVer!')