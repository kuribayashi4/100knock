from q30 import neko
connected_no = {sentence[i]['surface'] + "の" + sentence[i+2]['surface'] 
             for sentence in neko 
                 for i in range(len(sentence) - 2) 
                     if all((sentence[i]['pos'] == "名詞", sentence[i+1]['surface'] == "の",
                         sentence[i+2]['pos'] == "名詞"))}
print(connected_no)