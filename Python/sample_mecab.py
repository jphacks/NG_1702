from natto import MeCab
nm = MeCab()
text = "this is a test"
print nm.parse(text)
