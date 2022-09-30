import traceback
import requests

def convert(file_token):
    cookies = {
        'passport_web_did': '7130549151531827201',
        'QXV0aHpDb250ZXh0': 'e6247b47f5fe4f4797bdd1418288e3ce',
        'locale': 'zh-CN',
        'trust_browser_id': 'ec126e85-f8df-4a8c-8f21-cffb11665839',
        '__tea__ug__uid': '7130549122386855428',
        'is_anonymous_session': '',
        'lang': 'zh',
        'MONITOR_WEB_ID': '8c557655-1816-4759-91ad-17e471b73905',
        '_csrf_token': '9c1e5ab08685598e74d52a4dc61036642619b168-1662979237',
        'help_center_session': 'c126c9d2-19e9-4442-b265-270d66a7a42e',
        '_uuid_hera_ab_path_1': '7143827400751710236',
        'vt': '1',
        'et': '42187fdf6599d0d4105764f071fd5711',
        'ot': '06ec70c5edd6a6c6ef054a600ea23021',
        'landing_url': 'https://www.feishu.cn/product/docs',
        'Hm_lvt_e78c0cb1b97ef970304b53d2097845fd': '1663301934,1664505254',
        '_gid': 'GA1.2.127991392.1664505254',
        'session': 'XN0YXJ0-dcdr7041-4255-4d02-8b18-c01128c3f6cf-WVuZA',
        'session_list': 'XN0YXJ0-dcdr7041-4255-4d02-8b18-c01128c3f6cf-WVuZA_XN0YXJ0-15fgec87-c20d-4ded-808c-c18680fb20c2-WVuZA_XN0YXJ0-dcdr7041-4255-4d02-8b18-c01128c3f6cf-WVuZA',
        'js_version': '1',
        'Hm_lpvt_e78c0cb1b97ef970304b53d2097845fd': '1664506282',
        'sl_session': 'eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ1NTAwNjcsInVuaXQiOiJldV9uYyIsInJhdyI6eyJtZXRhIjoiQVdCY1h3eHkwa0FFWUZ4ZkRHY0J3QVFBQUFBQUFBQUFBR0wwekt5T2hJQUJBQUFBQUFBQUFBQUNLZ0VBUVVGQlFVRkJRVUZCUVVKcVJVMW5lbkJCUVVGSVFUMDkiLCJpZGMiOlsxLDJdLCJzdW0iOiJiYmQwODVlOGQ1OGMwZDkyZmM2NzdkZGE3NWFiZTk4Yjg3YWUwZWU4YTUwZjRmZmM4MmQxZmMxMTM1N2Y0YzQ5IiwibG9jIjoiemhfY24iLCJhcGMiOiJSZWxlYXNlIiwiaWF0IjoxNjY0NTA2ODY3fX0.NzVIL4Rd2LSZRggZHP4kcC4mcJ7-EAfi5KYgr__lIzzM9h38chC1THEeyh0DBjKAsybCB4JWKoFD5nuXMhABEQ',
        '_ga': 'GA1.2.1604574774.1660210350',
        '_ga_VPYRHN104D': 'GS1.1.1664505254.3.1.1664507428.0.0.0',
        'swp_csrf_token': 'c3f2e4b0-d6bb-4adc-b4d2-205e9705189d',
        't_beda37': '3e03e2c3de3e4313706401de8810ef4c7614e174d84d3c22488d8670695d5288',
    }


    headers = {
        'authority': 'tuc3es5ukv.feishu.cn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'cache-control': 'no-cache',
        'context': 'request_id=Hk5frCxBNMgx-f4f5e1c3f7e5721521ca196a63ead3d27e058b84;os=windows;app_version=1.0.7.8782;os_version=10;platform=web',
        'doc-biz': 'Lark',
        'doc-os': 'windows',
        'doc-platform': 'web',
        'f-version': 'docs-9-28-1664352681274',
        'origin': 'https://tuc3es5ukv.feishu.cn',
        'pragma': 'no-cache',
        'referer': f'https://tuc3es5ukv.feishu.cn/file/{file_token}',
        'request-id': 'Hk5frCxBNMgx-f4f5e1c3f7e5721521ca196a63ead3d27e058b84',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-csrftoken': '9c1e5ab08685598e74d52a4dc61036642619b168-1662979237',
        'x-request-id': 'Hk5frCxBNMgx-f4f5e1c3f7e5721521ca196a63ead3d27e058b84',
        'x-tt-logid': '02166450822736900000000000000000000ffffaa9463ac5a5ec6',
        'x-tt-trace-id': 'Hk5frCxBNMgx-f4f5e1c3f7e5721521ca196a63ead3d27e058b84',
    }

    json_data = {
        'file_token': file_token,
        'type': 'docx',
        'file_extension': 'md',
        'point': {
            'mount_type': 1,
            'mount_key': 'fldcnYylqxivPSlPzF5SCHKpdje',
        },
        'event_source': '3',
        'passback': '{"time_zone":"Etc/GMT-8"}',
    }
    try:
        response = requests.post('https://tuc3es5ukv.feishu.cn/space/api/import/create/', cookies=cookies, headers=headers, json=json_data)
        print(response.json())
    except:
        traceback.print_exc()


import requests

cookies = {
    'passport_web_did': '7130549151531827201',
    'QXV0aHpDb250ZXh0': 'e6247b47f5fe4f4797bdd1418288e3ce',
    'locale': 'zh-CN',
    'trust_browser_id': 'ec126e85-f8df-4a8c-8f21-cffb11665839',
    '__tea__ug__uid': '7130549122386855428',
    'is_anonymous_session': '',
    'lang': 'zh',
    'MONITOR_WEB_ID': '8c557655-1816-4759-91ad-17e471b73905',
    '_csrf_token': '9c1e5ab08685598e74d52a4dc61036642619b168-1662979237',
    'help_center_session': 'c126c9d2-19e9-4442-b265-270d66a7a42e',
    '_uuid_hera_ab_path_1': '7143827400751710236',
    'vt': '1',
    'et': '42187fdf6599d0d4105764f071fd5711',
    'ot': '06ec70c5edd6a6c6ef054a600ea23021',
    'landing_url': 'https://www.feishu.cn/product/docs',
    'Hm_lvt_e78c0cb1b97ef970304b53d2097845fd': '1663301934,1664505254',
    '_gid': 'GA1.2.127991392.1664505254',
    'session': 'XN0YXJ0-dcdr7041-4255-4d02-8b18-c01128c3f6cf-WVuZA',
    'session_list': 'XN0YXJ0-dcdr7041-4255-4d02-8b18-c01128c3f6cf-WVuZA_XN0YXJ0-15fgec87-c20d-4ded-808c-c18680fb20c2-WVuZA_XN0YXJ0-dcdr7041-4255-4d02-8b18-c01128c3f6cf-WVuZA',
    'js_version': '1',
    'Hm_lpvt_e78c0cb1b97ef970304b53d2097845fd': '1664506282',
    '_ga': 'GA1.2.1604574774.1660210350',
    '_ga_VPYRHN104D': 'GS1.1.1664511776.5.1.1664511777.0.0.0',
    'sl_session': 'eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ1NjAwMDksInVuaXQiOiJldV9uYyIsInJhdyI6eyJtZXRhIjoiQVdCY1h3eHkwa0FFWUZ4ZkRHY0J3QVFBQUFBQUFBQUFBR0wwekt5T2hJQUJBQUFBQUFBQUFBQUNLZ0VBUVVGQlFVRkJRVUZCUVVKcVJVMW5lbkJCUVVGSVFUMDkiLCJpZGMiOlsxLDJdLCJzdW0iOiJiYmQwODVlOGQ1OGMwZDkyZmM2NzdkZGE3NWFiZTk4Yjg3YWUwZWU4YTUwZjRmZmM4MmQxZmMxMTM1N2Y0YzQ5IiwibG9jIjoiemhfY24iLCJhcGMiOiJSZWxlYXNlIiwiaWF0IjoxNjY0NTE2ODA5fX0.26KQ2kgVbi3GVz0Pu4KPhIf1sothuZXGa2bTyAv7nuUDdNfcy3I4OLKZN6SpeefRBQAMyRXwciI5KtNG4WpQdg',
    'swp_csrf_token': '8075b7f1-2df5-4ee2-9209-3edc91805517',
    't_beda37': 'd52280435f3eda5b89b170db3023e1fa6a912d760dc72a11c35e67f470a0de62',
}
