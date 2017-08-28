#coding=utf8
import requests
import re
import time
from lxml import etree
import json

timestamp = int(time.time())

def request(name):
    url = 'http://weixin.sogou.com/weixin?query=%s'%name
    response = requests.get(url)
    content = response.content
    # print content
    tree = etree.HTML(content)
    mp_url = tree.xpath('''//p[@class="tit"]/a/@href''')
    return mp_url

def account_detail(mp_url):
    response = requests.get(mp_url[0])
    content = response.content
    # print content
    data = re.search('''var msgList = ([\s\S]*?)seajs''', content)
    if data:
        data = data.group(1)
        print data
    else:
        print 'not found'
        return
    pattern = re.compile(r'"content_url":"(.*?)"')
    url_list_1 = re.findall(pattern, data)
    print url_list_1
    url_list = []
    for each in url_list_1:
        url = 'https://mp.weixin.qq.com%s'%each
        url = url.replace('amp;',"")
        url_list.append(url)
    print len(url_list)
    for each in url_list:
        print each

    # print data[:-11]
    # data = json.loads(data.decode('utf-8').encode('utf-8'))
    # detail_list = data.get("list","")
    # print detail_list

if __name__ == '__main__':
    name = 'zhangzhaozhong45'
    mp_url = request(name)
    print mp_url
    account_detail(mp_url)