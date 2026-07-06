import pandas as pd

# Load the dataset
df = pd.read_csv('NLP_PROJECTS/spam_EMAIL_detection/dataset/spam.csv', encoding='latin-1')
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)

print(df.isnull().sum())
print(df.duplicated().sum())


#Cleaning Dataset

df.drop(columns = ["Unnamed: 2","Unnamed: 3","Unnamed: 4"],inplace = True)
df.rename(columns = {"v1":"label","v2":"text"},inplace=True)
print(df.columns)
print(df.head())
print(df.info())

#exploare data analytics
print(df["label"].value_counts(normalize=True)*100)

#creating new column 

df["text_length"] = df["text"].str.len()
print(df.columns)
print(df.head())

avg_text_length = df.groupby("label")["text_length"].mean()
print(avg_text_length)

#visualization

import matplotlib.pyplot as plt

plt.hist(df[df["label"] == "ham"]["text_length"], bins=50, alpha=0.7, label="Ham")

plt.hist(df[df["label"] == "spam"]["text_length"], bins=50, alpha=0.7, label="Spam")

plt.xlabel("Text Length")
plt.ylabel("Frequency")
plt.title("Ham vs Spam Message Length")

plt.legend()

plt.show()

#text lowercasing function using REGEX and splitting words using TOKENISATION
import re
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocessing(text):

    text = text.lower()

    text = re.sub(r"[^\w\s]", "", text)

    tokens = word_tokenize(text)

    tokens = [word for word in tokens if word not in stop_words]
    
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens


#new column

df["processed_text"] = df["text"].apply(preprocessing)

print(df[["text","processed_text"]].head())

