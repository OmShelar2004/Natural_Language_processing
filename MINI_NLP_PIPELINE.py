import string

text = "I AM Learning NLP!!! and it is AMAZING 123"

# Lowercase
text = text.lower()

# Remove punctuation
translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator)

# Tokenization
words = text.split()

# Remove numbers
words = [word for word in words if not word.isdigit()]

# Remove stopwords
stopwords = ["i", "am", "and", "it", "is"]

words = [word for word in words if word not in stopwords]

print(words)