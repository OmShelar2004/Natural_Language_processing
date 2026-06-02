#Extract contact numbers from the text

import re 

text = """
Call:
9876543210
9123456780
"""

phone = re.findall(r'\d{10}',text)

print(phone)