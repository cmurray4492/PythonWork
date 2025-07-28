my_word = input("Please enter a word: ")
my_word = my_word.upper()


for letter in my_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        print(letter)
