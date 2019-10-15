from ReadData import read_data
import jieba
import json
from pprint import pprint

data = read_data('Data.txt')
with open('out.json', 'w', encoding='utf-8') as wr:
    l = []
    for s in data:
        sc = jieba.lcut(s)
        d = {
            'sentence': s,
            'sentence_cut': sc
        }
        l.append(d)
    json.dump(l, wr, ensure_ascii=False, indent=4)
