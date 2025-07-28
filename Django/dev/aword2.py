my_word = input("Please enter a word: ")
my_word = my_word.upper()
final_word = ""

for letter in my_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    else:
        final_word += letter

print(final_word)
