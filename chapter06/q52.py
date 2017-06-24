from nltk.stem.porter import PorterStemmer
with open("work/nlp_parsed.txt", "r") as f1, open("work/nlp_stemmed.txt", "w") as f2:
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(word.strip()) for word in f1]
    f2.write("\n".join(stemmed))