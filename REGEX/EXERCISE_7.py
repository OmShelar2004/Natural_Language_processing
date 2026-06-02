import re 

text = """
Contact:
om@gmail.com
abc@yahoo.com

Phone:
9876543210
9123456780

Hashtags:
#Python #AI #MachineLearning

Mentions:
@OpenAI @Google
"""


extracted_emails = re.findall(r'\S+@\S+',text)
extracted_phone = re.findall(r'\d{10}',text)
extracted_hashtags = re.findall(r'#(\w+)',text)
extracted_mentions = re.findall(r'(?<!\w)@(\w+)',text)

print("Extracted Emails:", extracted_emails)
print("Extracted Phone Numbers:", extracted_phone)
print("Extracted Hashtags:", extracted_hashtags)
print("Extracted Mentions:", extracted_mentions)