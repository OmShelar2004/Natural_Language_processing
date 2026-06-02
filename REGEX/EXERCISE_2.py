#Extract Email IDs

import re 

text = """
Contact us:
abc@gmail.com
xyz@yahoo.com
"""

email_pattern = re.findall(r'\S+@\S+',text)

print(email_pattern)