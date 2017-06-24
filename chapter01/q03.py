import re
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
a = [len(re.findall('[a-zA-Z]', i)) for i in sentence.split()] #アルファベットの大文字小文字のみをカウント
print(a)