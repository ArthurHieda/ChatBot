import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer, WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
 
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

# Plotagem do gráfico de barras
plt.figure(figsize = (12,6))
plt.bar(frequencia.keys(), frequencia.values())
plt.xticks(rotation = 45)
plt.xlabel("Palavra")
plt.ylabel("Frequência")
plt.title("Frequência das Palavras no Texto")
plt.show()

# Plotagem do gráfico de pizza
plt.figure(figsize = (8, 8))
plt.pie(frequencia.values(), labels = frequencia.keys(), autopct = "%1.1f%%")
plt.title("Distribuição das Palavras no Texto")
plt.show()