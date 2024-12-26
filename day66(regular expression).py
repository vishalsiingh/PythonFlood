import re

pattern=" languages"
text='''Wikifunctions is a Wikimedia project for everyone to collaboratively create and 
maintain a library of code functions to support the Wikimedia projects and beyond,
in the world's natural and programming languages
'''
match=re.search(pattern,text)
print(match)