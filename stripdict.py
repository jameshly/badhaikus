import syllables
word_file = "words.txt"
open ('5words.txt', 'w').writelines(line for line in open('words.txt') if syllables.estimate(line) <= 5)