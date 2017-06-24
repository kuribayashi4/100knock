import gzip
import json
with gzip.open('data/jawiki-country.json.gz','rt') as f:
    for topic_str in f:
        topic_dict = json.loads(topic_str)
        if topic_dict['title'] == "イギリス":
            print(topic_dict['text'])