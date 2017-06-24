import matplotlib.pyplot as plt
from q36 import count_words
freq = [c for _, c in count_words.most_common()]
uniq_freq = sorted(freq, reverse = True)
x = [i for i in range(len(uniq_freq))]
plt.loglog(x,freq)
plt.xlabel("frequency rank", fontsize=20)
plt.ylabel("frequency", fontsize=20)
plt.show()