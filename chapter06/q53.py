import xml.etree.ElementTree as ET
tree = ET.parse('work/nlp.txt.xml')
root = tree.getroot()
for word in root.iter('word'):
    print(word.text)