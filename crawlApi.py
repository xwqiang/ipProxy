# -*- coding: utf-8 -*-
from util import robustCrawl, getHtmlTree, verifyProxy, validUsefulProxy

import requests, re

HEADER = {'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate, sdch',
          'Accept-Language': 'zh-CN,zh;q=0.8',
          }

'''
http://www.kuaidaili.com/ 这个地址爬不了了
http://www.goubanjia.com/free/gngn/index.shtml 也怕不了了
'''
@robustCrawl
def freeProxy1(proxy_number=100):
    """
    抓取代理66 http://www.66ip.cn/
    :param proxy_number: 代理数量
    :return:
    """
    # ip66_list = ("http://www.66ip.cn/{page}.html".format(page=pageNum) for pageNum in range(1, proxy_number + 1))
    ip66_list = ("http://www.66ip.cn/areaindex_1/{page}.html".format(page=pageNum) for pageNum in
                 range(1, proxy_number + 1))
    for ip66 in ip66_list:
        tree = getHtmlTree(ip66)
        proxy_list = tree.xpath('//div[@id="main"]//table//tr')
        for proxy in proxy_list:
            yield ':'.join(proxy.xpath('./td/text()')[0:2])


@robustCrawl
def freeProxy2(proxy_number=100):
    """
    抓取youdaili: http://www.youdaili.net/Daili/http/list_1.html
    :param proxy_number: 代理数量
    :return:
    """
    # 只查首页
    ip66_list = ("http://www.youdaili.net/Daili/http/list_{page}.html".format(page=pageNum) for pageNum in range(1, proxy_number + 1))
    for ip66 in ip66_list:
        tree = getHtmlTree(ip66)
        proxy_list = tree.xpath('//div[@class="chunlist"]/ul/li/p/a/@href')
        for page_url in proxy_list:
            detail_tree = getHtmlTree(page_url)
            content_list = detail_tree.xpath('//div[@class="content"]//p')
            for content in content_list:
                for proxy in  re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}',content.text):
                    yield proxy

@robustCrawl
def freeProxy3(proxy_number=100):
    """
    抓取西刺代理 http://api.xicidaili.com/free2016.txt 只支持GET
    :param proxy_number: 代理数量
    :return:
    """
    # 高密和普通代理
    xici_gaomi_list = ("http://www.xicidaili.com/nn/{page}".format(page=pageNum) for pageNum in range(1, proxy_number + 1))
    # xici_putong_list = ("http://www.xicidaili.com/nt/{page}".format(page=pageNum) for pageNum in range(1, proxy_number + 1))
    for ip66 in xici_gaomi_list:
        tree = getHtmlTree(ip66)
        proxy_list = tree.xpath('//table[@id="ip_list"]//tr')
        for page_url in proxy_list:
            yield ':'.join(page_url.xpath('.//td/text()')[0:2])



if __name__ == '__main__':
    for p in freeProxy3(proxy_number=1):
        print(p)
        if verifyProxy(p):
            print('validate proxy:', p)
            if validUsefulProxy(p):
                print(p)
