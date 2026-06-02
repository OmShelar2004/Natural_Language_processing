#Remove Special Characters using Regex

import re

text = "Hello@#$% World!! NLP123 is awesome."

clean_text = re.sub(r'[^a-zA-Z\s]','', text)
print(clean_text)