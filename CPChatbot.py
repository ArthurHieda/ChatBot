import nltk
import string
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import RSLPStemmer
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('punkt')

texto = "NASA has announced plans to launch a new spacecraft to study the atmosphere of Venus. The mission aims to provide insights into the planet's weather patterns and surface conditions."
print(f"Texto utilizado:{texto}")

# Tokenização
tokens = word_tokenize(texto)
tokens = [token.lower() for token in tokens if token not in string.punctuation]
print("Frase tokenizada:")
print(tokens)

# Stopwords
stop_words = set(stopwords.words('english'))
tokens = [token for token in tokens if token not in stop_words]

# Stemming
stemmer = RSLPStemmer()
tokens_stemmed = [stemmer.stem(token) for token in tokens]

# Frequência de palavras
contador = Counter(tokens_stemmed)
top_termos = contador.most_common(10)

print("Principais termos:")
for termo, frequencia in top_termos:
    print(f"Termo: {termo}, Frequência: {frequencia}")

# Análise de sentimento
analizador = SentimentIntensityAnalyzer()

pontuacao = analizador.polarity_scores(texto)
print("Análise de sentimento da sentença:")
print(pontuacao)

sentencas = sent_tokenize(texto)

pontuacao_sentencas = {}
for sentenca in sentencas:
    palavras_sentenca = word_tokenize(sentenca)
    pontuacao = sum(contador.get(stemmer.stem(palavra.lower()), 0) for palavra in palavras_sentenca)
    pontuacao_sentencas[sentenca] = pontuacao

sentencas_ordenadas = sorted(pontuacao_sentencas.items(), key=lambda x: x[1], reverse=True)
num_sentencas_resumo = 2

# Resumo Automático
resumo = [sentenca for sentenca, pontuacao in sentencas_ordenadas[:num_sentencas_resumo]]
print("\nResumo automático:")
for sentenca in resumo:
    print(sentenca)