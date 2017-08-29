#coding=utf8
import requests
import json

def http_api():
    url = 'http://lab.crossincode.com/proxy/get/'
    response = requests.get(url)
    content = response.content
    print content
    content = json.loads(content)
    proxies = content.get('proxies',[])
    for each in proxies:
        http = each.get('http',"")
        print http

def https_api():
    url = 'http://lab.crossincode.com/proxy/get/?num=5&head=https'
    response = requests.get(url)
    content = response.content
    print content
    content = json.loads(content)
    proxies = content.get('proxies',[])
    for each in proxies:
        https = each.get('https',"")
        print https

if __name__ == '__main__':
    http_api()
    # https_api()