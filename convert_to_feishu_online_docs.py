import json
from feishu import convert

with open('feishu_file_tokens.json', 'r', encoding='utf-8') as f:
    file_tokens = f.read()

    
file_tokens = json.loads(file_tokens)
for t in file_tokens:
    'https://tuc3es5ukv.feishu.cn/docx/RWcBdTuX4oQmHtxdsaUcfX6fnqh'
    if '/docx/' in t:
        continue
    if '/file/' in t:
        file_token = t.split('/')[-1]
        # print(file_token)
        convert(file_token)
        
