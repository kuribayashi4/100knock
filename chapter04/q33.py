from q30 import neko
verb_surface = {word['base'] for sentence in neko for word in sentence if word['pos1'] == "サ変接続"}