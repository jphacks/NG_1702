"""
Sample program for perse sites sentences to generate keywords for them.
"""
﻿from natto import MeCab
nm = MeCab()
text = "this is a test"
print nm.parse(text)
