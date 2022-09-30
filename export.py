import os
import re
import json
from logging import root
import requests

from urllib.parse import urljoin

root_url = 'https://www.yuque.com/api/v2/'

token = '8g04jZ0TaAmA7FQ95MhoNHkRsTntNWYcQ8hOor9f'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
 
    'X-Auth-Token': token
}


def get_user():
    url = urljoin(root_url, 'user')
    resp = requests.get(url, headers=headers)
    return resp.json()

def get_repo(user_id, name):
    url = urljoin(root_url, f'users/{user_id}/repos')
    # print(url)
    resp = requests.get(url, headers=headers)
    result = resp.json()
    for d in result.get('data', []):
        if d['name'] == name:
            # print(d)
            return d['id']

def get_docs(repo_id):
    url = urljoin(root_url, f'repos/{repo_id}/docs')
    resp = requests.get(url, headers=headers)
    result = resp.json()
    return result



def save_docs_list_to_json(name, namespace):
    user = get_user()
    # print(user)
    user_id = user.get('data', {}).get('id')
    repo_id = get_repo(user_id, )
    docs = get_docs(repo_id)
    # print(docs)

    with open('docs_list.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(docs, ensure_ascii=False, indent=4))


def save_docs(namespace):

    save_docs_dir = 'docs'
    if not os.path.exists(save_docs_dir):
        os.makedirs(save_docs_dir)


    with open('docs_list.json', 'r', encoding='utf-8') as f:
        docs_list = f.read()

    docs_list = json.loads(docs_list).get('data', [])
    # docs_list = sorted(docs_list, lambda x: x['created_at'])
    for d in docs_list:
        slug = d['slug']
        title = d['title']
        url = urljoin(root_url, f'repos/{namespace}/docs/{slug}')
        resp = requests.get(url, headers=headers, params={'raw': 1})
        result = resp.json()
        markdown_content = result.get('data', {}).get('body', '')
         # 正则去除语雀导出的<a>标签
        markdown_content = re.sub("<a name=\".*\"></a>","", markdown_content) 
        title = title.replace('/', ',')
        with open(os.path.join(save_docs_dir, f'{title}.md'), 'w', encoding='utf-8') as f:
            f.write(markdown_content)


if __name__ == '__main__':
    name = '网络爬虫技术'
    namespace = 'erliang-vtlak/aufz2f'
    save_docs_list_to_json(name=name)
    save_docs(namespace)
