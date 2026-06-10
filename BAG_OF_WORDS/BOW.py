from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "I love NLP",
    "I love Python"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(sentences)

print(vectorizer.get_feature_names_out())