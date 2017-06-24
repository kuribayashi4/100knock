import xml.etree.ElementTree as ET
tree = ET.parse('work/nlp.txt.xml')
root = tree.getroot()
for coref in root.findall('.//coreference/coreference'):
    rep_mention = coref.find("*[@representative='true']")
    for mention in coref:
        word_start, word_end = mention[-1].text.split()[0], mention[-1].text.split()[-1]
        i_sent, i_start, i_end = mention[0].text, mention[1].text, str(int(mention[2].text)-1)
        root.find(".//sentence[@id='{}']/tokens/token[@id='{}']".format(i_sent, i_start))[0].text \
        = " [" + rep_mention[-1].text + "](" + word_start
        root.find(".//sentence[@id='{}']/tokens/token[@id='{}']".format(i_sent, i_end))[0].text \
        = word_end + ")"
tree.write('work/nlp_coreference.txt.xml')

#出力の整形
with open('work/nlp_coreferene.txt', 'w') as f:
    tree = ET.parse('work/nlp_coreference.txt.xml')
    root = tree.getroot()
    for sentence in root.iter('sentence'):
        for word in sentence.iter('word'):
            f.write(word.text + " ")
        f.write("\n")
! gsed -E "s/\s(\W)/\1/g" work/nlp_coreferene.txt