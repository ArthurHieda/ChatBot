import nltk
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize

#Baixar recursus adicionais do LTK
nltk.download('rslp')

#Instanciar o stemmer RSLP
stemmer = RSLPStemmer()

#Texto de exemplo
texto = "Eu estava pensando que poderia ter sido melhor."

#Tokenizar o texto em palavras
palavras = word_tokenize(texto, language="portuguese")

#Aplicar stemming às palavras
stemmed_palavras = [stemmer.stem(palavra) for palavra in palavras]

#Juntar as palavras stemizadas em um texto
stemmed_texto = " ".join(stemmed_palavras)

print(f"Texto original: {texto}")
print(f"\nTexto com stemming: {stemmed_texto}")