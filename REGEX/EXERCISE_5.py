#extract mentions from a text using regex

import re 

text = "@elonmusk launched a rocket with @spacex"

mentions = re.findall(r'@(\w+)',text)

print(mentions)
