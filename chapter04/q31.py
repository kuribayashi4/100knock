from q30 import neko
verb_surface = {word['surface'] for sentence in neko for word in sentence if word['pos'] == "動詞"}
print(verb_surface)