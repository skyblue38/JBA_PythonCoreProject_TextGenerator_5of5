import re

template = '[B-N][AaEeIiOoUu]'
name = input()
if re.match(template, name) is not None:
    print("Suitable!")
