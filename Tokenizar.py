import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

print(stopwords.words("portuguese"))

text = "A filha xuxa se chama sasha ela tem uma casa suja com um chão sujo"
tokens = word_tokenize(text, language="portuguese")
print(tokens)