import xml.etree.ElementTree as ET
tree = ET.parse('work/nlp.txt.xml')
root = tree.getroot()
for token in root.findall(".//*[NER='PERSON']"): 
    print(token[0].text)