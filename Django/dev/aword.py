the_word = input("Please enter a word: ")
the_word = the_word.lower()
new_word = []

for letter in the_word:
    if letter not in ['a', 'e', 'i', 'o', 'u']:
        new_word.append(letter)

new_word = ''.join(new_word)

print(new_word)
