import re
import pprint
import requests
dict_in_json={}
def search_json(json, key):
    for k,v in json.items():
        if isinstance(v,dict):
            search_json(v,key)
        elif isinstance(v,list):
            for dictionary in v:
                search_json(dictionary,key)
        else:
            dict_in_json.update({k:v})
    if key in dict_in_json:
        return dict_in_json['{}'.format(key)]
            
url = 'https://en.wikipedia.org/w/api.php'
payload = {"action": "query",
           "titles": "File:{}".format(basic_info_dict[u"国旗画像"]),
           "prop": "imageinfo",
           "format": "json",
           "iiprop": "url"}
json_data = requests.get(url, params=payload).json()
print(json_data) 
print(search_json(json_data,"url"))