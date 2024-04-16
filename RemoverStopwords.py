import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Carregar lista de stopwords para o potuguês
stopwords = set(stopwords.words("portuguese"))

#Texto de exemplo
text = "Isso é um exemplo de uso para remoção de stopwords em um texto no idioma português"

#Tokenizar o texto em palavras
words = word_tokenize(text)

#Remover stopwords
filtered_words = [word for word in words if word.lower() not in stopwords]

#Juntar as palavras filtradas de volta em um texto
filtered_text = ' '.join(filtered_words)

print("Texto original")
print(text)
print("\nTexto com stopwords removidas:")
print(filtered_text)