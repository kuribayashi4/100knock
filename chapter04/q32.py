from q30 import neko
verb_base = {word['base'] for sentence in neko for word in sentence if word['pos'] == "動詞"}
print(verb_base)