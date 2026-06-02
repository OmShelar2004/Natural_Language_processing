#Exercise 1: Lowercase Conversion

text = "I **@LOVE ,23MACHINE LEarning!!!** and I34 am learning NLP and 69 it is fun"

lowercase_text = text.lower()
print(lowercase_text)


#Exercise 2: Remove Punctuation

import string

for p in string.punctuation:
   lowercase_text= lowercase_text.replace(p,"")
   
print(lowercase_text)


#Exercise 3: Tokenization

tokens = lowercase_text.split()
print(tokens)

#Exercise 4: Count Number of Words

word_count = len(tokens)
print(word_count)

#Exercise 5: Remove Stop Words

stop_words = ["i", "and", "am", "it", "is"]

words = tokens

result = []

for word in words:
   if word not in stop_words:
      result.append(word)


print(result)      


#Exercise 6: Word Frequency Count
from collections import Counter

freq = Counter(lowercase_text.split())

print(freq)

#Exercise 7: most common word

most_common_word = freq.most_common()
print(most_common_word[0][0])

#Exercise 8: remove numbers


text2 = "My age is 21 and weight is 65"
words = text2.split()

result = []

for word in words:
    if not word.isdigit():
        result.append(word)

print(" ".join(result))

#Exercise 9: Stemming

from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "plays"]

for word in words:
      print(ps.stem(word))