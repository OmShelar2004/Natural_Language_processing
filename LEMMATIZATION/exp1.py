from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cars"))
print(lemmatizer.lemmatize("playings"))

print(lemmatizer.lemmatize("playing", pos="v"))

print(lemmatizer.lemmatize("better",pos="a"))
print(lemmatizer.lemmatize("children"))
print(lemmatizer.lemmatize("mice"))
print(lemmatizer.lemmatize("geese"))