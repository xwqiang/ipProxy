import crawlApi
import util

import db


def refreshProxy(proxy_list, source):
    for proxy1 in proxy_list:
        if util.verifyProxy(proxy1):
            sql = 'insert ignore into http_proxy(proxy_addr,valid,source_site,created_time,modified_time) values("{proxy}",0,"{source_site}",now(),now())'.format(
                proxy=proxy1, source_site=source)
            print(sql)
            db.execute(sql)


if __name__ == '__main__':
    refreshProxy(crawlApi.freeProxy1(), 'www.66ip.cn')
    refreshProxy(crawlApi.freeProxy2(), 'www.youdaili.net')
    refreshProxy(crawlApi.freeProxy3(), 'www.xicidaili.com')
