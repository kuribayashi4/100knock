import matplotlib.pyplot as plt
from q36 import count_words
y = [c for _, c in count_words.most_common()]
plt.hist(y,bins=10, log=True)
plt.xlabel("frequency", fontsize=20)
plt.ylabel("The number of word types", fontsize=20)
plt.show()