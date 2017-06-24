from q30 import neko
verb_sahen = {word['base'] for sentence in neko for word in sentence if word['pos1'] == "サ変接続"}
print(verb_sahen)