from collections import Counter
from q30 import neko

all_words = (word['base'] for sentence in neko for word in sentence)
count_words = Counter(all_words)
print(count_words.most_common(10))