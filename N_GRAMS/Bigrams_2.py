from nltk.util import ngrams

text = "Python is fun"

words = text.split()

bigrams = list(ngrams(words,2))

print(bigrams)