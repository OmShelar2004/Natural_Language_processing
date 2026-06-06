from nltk.util import ngrams

text = "I love machine learning"

words = text.split()

bigrams = list(ngrams(words,2))

print(bigrams)
