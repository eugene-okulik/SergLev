text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,'
        ' dignissim vitae libero')

words = text.split()
words_ing = []
for word in words:
    if word.endswith(',') or word.endswith('.'):
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
    words_ing.append(new_word)
print(' '.join(words_ing))
