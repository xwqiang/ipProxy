# -*- coding: utf-8 -*-
import requests

from lxml import etree


def robustCrawl(func):
    def decorate(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("sorry, 抓取出错。错误原因:")
            print(e)

    return decorate


def getHtmlTree(url):
    header = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }

    html = requests.get(url, headers=header, timeout=30).content
    return etree.HTML(html)


def verifyProxy(proxy):
    """
    检查代理格式
    :param proxy:
    :return:
    """
    import re
    verify_regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}"
    return True if re.findall(verify_regex, proxy) else False


def validUsefulProxy(proxy):
    """
    检验代理可以性
    :param proxy:
    :return:
    """
    proxies = {"http": "http://{proxy}".format(proxy=proxy),
               "https": "https://{proxy}".format(proxy=proxy)}
    try:
        # 超过30秒的代理就不要了
        r = requests.get('https://www.baidu.com/', proxies=proxies, timeout=10, verify=False)
        if r.status_code == 200:
            return True
    except Exception:
        return False
