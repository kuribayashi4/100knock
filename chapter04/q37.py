import matplotlib.pyplot as plt
import seaborn as sns
from q36 import count_words
sns.set(font='AppleGothic')

label, y = [], []
for word, i in count_words.most_common(10):
    label.append(word)
    y.append(i)
x = [i for i in range(10)]
plt.bar(x, y, tick_label =label, align="center")
plt.ylabel("frequency", fontsize=20)
plt.show()