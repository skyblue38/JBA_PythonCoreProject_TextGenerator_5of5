import re

# your code here
word = input()
template = '.*-.*'
if re.match(template, word) is None:
    print('False')
else:
    print('True')
