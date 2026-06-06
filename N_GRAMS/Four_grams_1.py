from nltk.util import ngrams

text = "AI will change the future"

words = text.split()

four_grams = list(ngrams(words,4))

print(four_grams)