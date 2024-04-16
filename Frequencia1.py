import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer, WordNetLemmatizer
from collections import Counter
 
# Baixar recursos adicionais do NLTK
nltk.download("punkt")
nltk.download("stopwords")
 
# Texto de exemplo
texto = "O cachorro correu pelo parque. O gato dormiu na poltrona. O cachorro latiu para o gato."
 
# Tokenização
tokens = word_tokenize(texto.lower(), language = "portuguese")
 
# Remoção da pontuação e stopwords (stopwords definidas no Início)
pontuacao = set(string.punctuation)
stopwords = set(stopwords.words("portuguese"))
tokens_filtrados = [palavra for palavra in tokens if palavra not in pontuacao and palavra not in stopwords]
 
# Contagem de frequência
frequencia = Counter(tokens_filtrados)
 
# Exibição dos resultados
print("Frequência das palavras: ")
for pal, freq in frequencia.items():
    print(f"{pal}: {freq}")