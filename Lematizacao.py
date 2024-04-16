import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

#Baixar recursos adicionais do NLTK
nltk.download("wordnet")

#Instanciar o lematizador Wordnet
lemmaizer = WordNetLemmatizer()

#Texto de exmplo
texto = "O novo livro do autor seria lançado em breve na feira do livro."

#Tokenizar o texto em palavras
palavras = word_tokenize(texto, language="portuguese")

#Aplicar lematização às palavras
lemmatized_palavras = [lemmaizer.lemmatize(palavra) for palavra in palavras]

#Jntar as palavras lematizadas em texto
lemmatized_texto = ' '.join(lemmatized_palavras)

print(f"Texto original: {texto}")
print(f"Texto com o lematizado: {lemmatized_texto}")