from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()

words = [
    "cars",
    "children",
    "mice",
    "running",
    "played",
    "studies"
]

for word in words:
    if word.endswith("ing") or word.endswith("ed") or word.endswith("ies"):
        print(f"{word} -> {lemmatizer.lemmatize(word, pos='v')}")
    else:
        print(f"{word} -> {lemmatizer.lemmatize(word)}")    