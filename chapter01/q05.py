def n_gram(words, n):
    return [words[i:i+n] for i in range(len(words) - n + 1)]
msg = "I am an NLPer"
print(n_gram(msg.split(), 2),'\n', n_gram(msg, 2))