##Email,phone number, hashtags, mentions##

import re 

tweet = """
Hey @OpenAI!
Learning #NLP is amazing.

Contact me at om@gmail.com
Call 9876543210
"""
extracted_emails = re.findall(r'\S+@\S+',tweet)
extracted_phone = re.findall(r'\d{10}',tweet)
extracted_hashtags = re.findall(r'#(\w+)',tweet)
extracted_mentions = re.findall(r'(?<!\w)@(\w+)',tweet)

print("Extracted Emails:", extracted_emails)
print("Extracted Phone Numbers:", extracted_phone)
print("Extracted Hashtags:", extracted_hashtags)
print("Extracted Mentions:", extracted_mentions)


import re

text = "AI AI ML AI NLP ML"

result = re.findall(r'AI', text)

print(result)
print(len(result))