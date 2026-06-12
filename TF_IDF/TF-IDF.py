from  sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "AI is amazing",
    "AI is powerful",
    "AI is revolutionary"
]

vectorizer = TfidfVectorizer()

x = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())   
print(x.toarray())