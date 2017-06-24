import random
def random_sort(item):
    random.shuffle(item)
    return item
def typoglycemia(msg):
    return " ".join(word if len(word) <= 4 
                        else (word[0] + "".join(random_sort(list(word[1:-1]))) + word[-1]) 
                            for word in msg.split())   

msg = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(msg))