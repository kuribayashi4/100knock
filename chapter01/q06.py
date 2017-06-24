def n_gram(words, n):
    return [words[i:i+n] for i in range(len(words) - n + 1)]
str_1 = "paraparaparadise"
str_2 = "paragraph"
X = set(n_gram(str_1, 2)) #set型にすることで集合演算が可能に、重複する要素は削除
Y = set(n_gram(str_2, 2))
print("X = ", X)
print("Y = ", Y)
print("X|Y = " , X|Y) #和集合
print("X&Y = ", X&Y) #積集合
print("X-Y = ", X-Y) #差集合X-Y
print("Y-X = ", Y-X) #差集合Y-X
if 'se' in X:
    print("'se' exists in X")
else:
    print("'se' doesn't exist in X")
if 'se' in Y:
    print("'se' exists in Y")
else:
    print("'se' doesn't exist in Y")