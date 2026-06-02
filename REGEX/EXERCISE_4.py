#extract # hashtags from a text using regex

import re 

text = "Learning #Python #AI #MachineLearning"

hashtags = re.findall(r'#(\w+)',text)

print(hashtags)