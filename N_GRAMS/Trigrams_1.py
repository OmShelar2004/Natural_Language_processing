from nltk.util import ngrams

text = "I love machine learning"

words = text.split()

trigrams = list(ngrams(words,3))

print(trigrams)