# coding : utf-8
import json
import requests
import copy

feed_url = 'https://index.baidu.com/api/FeedSearchApi/getFeedIndex' #资讯指数
search_url = 'https://index.baidu.com/api/SearchApi/index' #搜索指数
people_url = 'https://index.baidu.com/api/SocialApi/baseAttributes' #人群画像
ratio_url = 'https://index.baidu.com/api/WordGraph/multi' #需求图谱

def parse_people(name):
    age_dic = {}
    age_list = []
    gender_dic = {}
    gender_list = []
    headers = {
        'Cookie': 'BIDUPSID=66C11D81E70144950900E4250FD539A1; PSTM=1645621822; BAIDUID=66C11D81E7014495E660CDBB3FAD4F21:FG=1; __yjs_duid=1_379403d62856365268bc2ed8417321b31645622710389; BDUSS=w0ZXRqY2p2VDRGZ1pIVHZMOWVHbG5ZflFyVlJCNkdqQTZaRlhoRkR0TGV3ajFpSVFBQUFBJCQAAAAAAAAAAAEAAACMBHk6a2FiYTU2NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN41FmLeNRZiV2; BDUSS_BFESS=w0ZXRqY2p2VDRGZ1pIVHZMOWVHbG5ZflFyVlJCNkdqQTZaRlhoRkR0TGV3ajFpSVFBQUFBJCQAAAAAAAAAAAEAAACMBHk6a2FiYTU2NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN41FmLeNRZiV2; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1648300497; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%22981009548%22%2C%22scope%22%3A1%7D%7D; bdindexid=o7ghlt6ih45hnvo0qf7julg5f4; H_PS_PSSID=36159_31253_36167_34584_36120_36033_36125_35993_35956_35315_26350_36112_35869_36100_36061; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=1; PSINO=5; BAIDUID_BFESS=F702DD6521519DF691E480EF607A16BA:FG=1; ZD_ENTRY=baidu; BA_HECTOR=0h0k8505ah2l0k2kfq1h405k20r; RT="sl=0&ss=l18zten5&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=61o0xl56h85"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1648369415; ab_sr=1.0.1_YjE4Njc1NjBmOTdmNTYzYWRjMjMwYzBmYTQ5NzUzYjNlYWRiMjNjNmJiNDRlNTY4ODA5NDg0NTE5ZDQ3NWMyODE2ZTJiYTdlZmNlMmIyYjEzNTVhNjM2YzQ5NzY3MzU5MzVhYzAyYTlkMjc3YzQwZDM5MWVkOGQyNmIwMTJhZTk4MDgyNDZhOTFlNTQ2MzJjNzQ3ZWMzNmRiYjYzNmIzNQ==; __yjs_st=2_ZWY4ZmU3Y2IxYjhlYWUxYjU5ZjYzZDM0NmQxZGRhMTYwZDNkZWVlNjE2MGIzMjRmOTk2NzQzMjYzNGNlYjEyMjEwOWM1MjA0ZTFiZmU4ZDAwZDQ4MWE4ZWIzM2I4ZDU3OTUwYTY0OWUzMTdiNTE4YWU4NzY5NzhlZTdiMDI0YzJiMDE4NWU2MjUxNjhkZmRkMGUzM2UzODU3YjAzMmE4NzFkYWVjNTIxMjlhMDEzYjg1NWY1NGMxOTNhY2NlNjMzXzdfYzkwZTdiMmY=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
        'Referer': 'https://index.baidu.com/v2/main/index.html'
    }
    params = {
        'wordlist[]':name
    }
    response_text = requests.get(url = people_url, headers = headers , params = params)
    response = response_text.json()
    for age in response['data']['result'][0]['age']:
        age_dic['%s年龄范围'%name] = age['desc']
        age_dic['%s年龄比例'%name] = age['rate']
        age_dic['%s年龄tgi' % name] = age['tgi']
        print(age_dic)
        age_list.append(copy.deepcopy(age_dic))
    print(age_list)
    for gender in response['data']['result'][0]['gender']:
        gender_dic['%s性别' % name] = gender['desc']
        gender_dic['%s性别比例' % name] = gender['rate']
        gender_dic['%s性别tgi' % name] = gender['tgi']
        print(gender_dic)
        gender_list.append(copy.deepcopy(gender_dic))
    print(gender_list)

def parse_ratio(name):
    dic = {}
    list = []
    headers = {
        'Cookie': 'BIDUPSID=66C11D81E70144950900E4250FD539A1; PSTM=1645621822; BAIDUID=66C11D81E7014495E660CDBB3FAD4F21:FG=1; __yjs_duid=1_379403d62856365268bc2ed8417321b31645622710389; BDUSS=w0ZXRqY2p2VDRGZ1pIVHZMOWVHbG5ZflFyVlJCNkdqQTZaRlhoRkR0TGV3ajFpSVFBQUFBJCQAAAAAAAAAAAEAAACMBHk6a2FiYTU2NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN41FmLeNRZiV2; BDUSS_BFESS=w0ZXRqY2p2VDRGZ1pIVHZMOWVHbG5ZflFyVlJCNkdqQTZaRlhoRkR0TGV3ajFpSVFBQUFBJCQAAAAAAAAAAAEAAACMBHk6a2FiYTU2NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN41FmLeNRZiV2; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1648300497; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%22981009548%22%2C%22scope%22%3A1%7D%7D; bdindexid=o7ghlt6ih45hnvo0qf7julg5f4; H_PS_PSSID=36159_31253_36167_34584_36120_36033_36125_35993_35956_35315_26350_36112_35869_36100_36061; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=1; PSINO=5; BAIDUID_BFESS=F702DD6521519DF691E480EF607A16BA:FG=1; ZD_ENTRY=baidu; BA_HECTOR=0h0k8505ah2l0k2kfq1h405k20r; RT="sl=0&ss=l18zten5&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=61o0xl56h85"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1648369415; ab_sr=1.0.1_YjE4Njc1NjBmOTdmNTYzYWRjMjMwYzBmYTQ5NzUzYjNlYWRiMjNjNmJiNDRlNTY4ODA5NDg0NTE5ZDQ3NWMyODE2ZTJiYTdlZmNlMmIyYjEzNTVhNjM2YzQ5NzY3MzU5MzVhYzAyYTlkMjc3YzQwZDM5MWVkOGQyNmIwMTJhZTk4MDgyNDZhOTFlNTQ2MzJjNzQ3ZWMzNmRiYjYzNmIzNQ==; __yjs_st=2_ZWY4ZmU3Y2IxYjhlYWUxYjU5ZjYzZDM0NmQxZGRhMTYwZDNkZWVlNjE2MGIzMjRmOTk2NzQzMjYzNGNlYjEyMjEwOWM1MjA0ZTFiZmU4ZDAwZDQ4MWE4ZWIzM2I4ZDU3OTUwYTY0OWUzMTdiNTE4YWU4NzY5NzhlZTdiMDI0YzJiMDE4NWU2MjUxNjhkZmRkMGUzM2UzODU3YjAzMmE4NzFkYWVjNTIxMjlhMDEzYjg1NWY1NGMxOTNhY2NlNjMzXzdfYzkwZTdiMmY=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
        'Referer': 'https://index.baidu.com/v2/main/index.html'
    }
    params = {
        'wordlist[]': 'python'
    }
    params['wordlist[]'] = name
    response_text = requests.get(url = ratio_url, headers = headers , params = params)
    response = response_text.json()
    for data in response['data']['wordlist'][0]['wordGraph']:
        dic['关键词'] = response['data']['wordlist'][0]['keyword']
        dic['相关词'] = data['word']
        dic['搜索指数'] = data['pv']
        dic['搜索趋势'] = data['ratio']
        dic['相关性指数'] = data['sim']
        print(dic)
        list.append(copy.deepcopy(dic))
    print(list)


def parse_feed(name1,name2):
    dic = {}
    headers = {
        'Cookie': 'BIDUPSID=66C11D81E70144950900E4250FD539A1; PSTM=1645621822; BAIDUID=66C11D81E7014495E660CDBB3FAD4F21:FG=1; __yjs_duid=1_379403d62856365268bc2ed8417321b31645622710389; BDUSS=w0ZXRqY2p2VDRGZ1pIVHZMOWVHbG5ZflFyVlJCNkdqQTZaRlhoRkR0TGV3ajFpSVFBQUFBJCQAAAAAAAAAAAEAAACMBHk6a2FiYTU2NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN41FmLeNRZiV2; BDUSS_BFESS=w0ZXRqY2p2VDRGZ1pIVHZMOWVHbG5ZflFyVlJCNkdqQTZaRlhoRkR0TGV3ajFpSVFBQUFBJCQAAAAAAAAAAAEAAACMBHk6a2FiYTU2NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN41FmLeNRZiV2; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1648300497; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%22981009548%22%2C%22scope%22%3A1%7D%7D; bdindexid=o7ghlt6ih45hnvo0qf7julg5f4; H_PS_PSSID=36159_31253_36167_34584_36120_36033_36125_35993_35956_35315_26350_36112_35869_36100_36061; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=1; PSINO=5; BAIDUID_BFESS=F702DD6521519DF691E480EF607A16BA:FG=1; ZD_ENTRY=baidu; BA_HECTOR=0h0k8505ah2l0k2kfq1h405k20r; RT="sl=0&ss=l18zten5&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=61o0xl56h85"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1648369415; ab_sr=1.0.1_YjE4Njc1NjBmOTdmNTYzYWRjMjMwYzBmYTQ5NzUzYjNlYWRiMjNjNmJiNDRlNTY4ODA5NDg0NTE5ZDQ3NWMyODE2ZTJiYTdlZmNlMmIyYjEzNTVhNjM2YzQ5NzY3MzU5MzVhYzAyYTlkMjc3YzQwZDM5MWVkOGQyNmIwMTJhZTk4MDgyNDZhOTFlNTQ2MzJjNzQ3ZWMzNmRiYjYzNmIzNQ==; __yjs_st=2_ZWY4ZmU3Y2IxYjhlYWUxYjU5ZjYzZDM0NmQxZGRhMTYwZDNkZWVlNjE2MGIzMjRmOTk2NzQzMjYzNGNlYjEyMjEwOWM1MjA0ZTFiZmU4ZDAwZDQ4MWE4ZWIzM2I4ZDU3OTUwYTY0OWUzMTdiNTE4YWU4NzY5NzhlZTdiMDI0YzJiMDE4NWU2MjUxNjhkZmRkMGUzM2UzODU3YjAzMmE4NzFkYWVjNTIxMjlhMDEzYjg1NWY1NGMxOTNhY2NlNjMzXzdfYzkwZTdiMmY=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
        'Referer': 'https://index.baidu.com/v2/main/index.html'
    }
    params = {
        'area': '0',
        'word': '[[{"name": "python", "wordType": 1}], [{"name": "java", "wordType": 1}]]',
        'days': '30'
    }
    params['word'] = '[[{"name": "%s", "wordType": 1}], [{"name": "%s", "wordType": 1}]]'%(name1,name2)
    response_text = requests.get(url = feed_url, headers = headers , params = params)
    response = response_text.json()
    dic['1_name'] = response['data']['index'][0]['key'][0]['name']
    dic['日均值1'] = response['data']['index'][0]['generalRatio']['avg']
    dic['同比1'] = response['data']['index'][0]['generalRatio']['yoy']
    dic['环比1'] = response['data']['index'][0]['generalRatio']['qoq']
    dic['2_name'] = response['data']['index'][1]['key'][0]['name']
    dic['日均值2'] = response['data']['index'][1]['generalRatio']['avg']
    dic['同比2'] = response['data']['index'][1]['generalRatio']['yoy']
    dic['环比2'] = response['data']['index'][1]['generalRatio']['qoq']
    print(dic)


def parse_search(name1,name2):
    dic = {}
    headers = {
        'Cookie': 'BIDUPSID=66C11D81E70144950900E4250FD539A1; PSTM=1645621822; BAIDUID=66C11D81E7014495E660CDBB3FAD4F21:FG=1; __yjs_duid=1_379403d62856365268bc2ed8417321b31645622710389; BDUSS=w0ZXRqY2p2VDRGZ1pIVHZMOWVHbG5ZflFyVlJCNkdqQTZaRlhoRkR0TGV3ajFpSVFBQUFBJCQAAAAAAAAAAAEAAACMBHk6a2FiYTU2NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN41FmLeNRZiV2; BDUSS_BFESS=w0ZXRqY2p2VDRGZ1pIVHZMOWVHbG5ZflFyVlJCNkdqQTZaRlhoRkR0TGV3ajFpSVFBQUFBJCQAAAAAAAAAAAEAAACMBHk6a2FiYTU2NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN41FmLeNRZiV2; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1648300497; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%22981009548%22%2C%22scope%22%3A1%7D%7D; bdindexid=o7ghlt6ih45hnvo0qf7julg5f4; H_PS_PSSID=36159_31253_36167_34584_36120_36033_36125_35993_35956_35315_26350_36112_35869_36100_36061; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=1; PSINO=5; BAIDUID_BFESS=F702DD6521519DF691E480EF607A16BA:FG=1; ZD_ENTRY=baidu; BA_HECTOR=0h0k8505ah2l0k2kfq1h405k20r; RT="sl=0&ss=l18zten5&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&z=1&dm=baidu.com&si=61o0xl56h85"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1648369415; ab_sr=1.0.1_YjE4Njc1NjBmOTdmNTYzYWRjMjMwYzBmYTQ5NzUzYjNlYWRiMjNjNmJiNDRlNTY4ODA5NDg0NTE5ZDQ3NWMyODE2ZTJiYTdlZmNlMmIyYjEzNTVhNjM2YzQ5NzY3MzU5MzVhYzAyYTlkMjc3YzQwZDM5MWVkOGQyNmIwMTJhZTk4MDgyNDZhOTFlNTQ2MzJjNzQ3ZWMzNmRiYjYzNmIzNQ==; __yjs_st=2_ZWY4ZmU3Y2IxYjhlYWUxYjU5ZjYzZDM0NmQxZGRhMTYwZDNkZWVlNjE2MGIzMjRmOTk2NzQzMjYzNGNlYjEyMjEwOWM1MjA0ZTFiZmU4ZDAwZDQ4MWE4ZWIzM2I4ZDU3OTUwYTY0OWUzMTdiNTE4YWU4NzY5NzhlZTdiMDI0YzJiMDE4NWU2MjUxNjhkZmRkMGUzM2UzODU3YjAzMmE4NzFkYWVjNTIxMjlhMDEzYjg1NWY1NGMxOTNhY2NlNjMzXzdfYzkwZTdiMmY=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
        'Referer': 'https://index.baidu.com/v2/main/index.html'
    }
    params = {
        'area': '0',
        'word': '[[{"name": "python", "wordType": 1}], [{"name": "java", "wordType": 1}]]',
        'days': '30'
    }
    params['word'] = '[[{"name": "%s", "wordType": 1}], [{"name": "%s", "wordType": 1}]]'%(name1,name2)
    response_text = requests.get(url = search_url, headers = headers , params = params)
    response = response_text.json()
    dic['1_name'] = response['data']['generalRatio'][0]['word'][0]['name']
    dic['整体日均值1'] = response['data']['generalRatio'][0]['all']['avg']
    dic['整体同比1'] = response['data']['generalRatio'][0]['all']['yoy']
    dic['整体环比1'] = response['data']['generalRatio'][0]['all']['qoq']
    dic['移动日均值1'] = response['data']['generalRatio'][0]['wise']['avg']
    dic['移动同比1'] = response['data']['generalRatio'][0]['wise']['yoy']
    dic['移动环比1'] = response['data']['generalRatio'][0]['wise']['qoq']
    dic['2_name'] = response['data']['generalRatio'][1]['word'][0]['name']
    dic['整体日均值2'] = response['data']['generalRatio'][1]['all']['avg']
    dic['整体同比2'] = response['data']['generalRatio'][1]['all']['yoy']
    dic['整体环比2'] = response['data']['generalRatio'][1]['all']['qoq']
    dic['移动日均值2'] = response['data']['generalRatio'][1]['wise']['avg']
    dic['移动同比2'] = response['data']['generalRatio'][1]['wise']['yoy']
    dic['移动环比2'] = response['data']['generalRatio'][1]['wise']['qoq']
    print(dic)
parse_people('python')




