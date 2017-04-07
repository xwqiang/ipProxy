import crawlApi
import util

import db


def refresh(proxy_list,source):
    for proxy1 in proxy_list:
        if util.verifyProxy(proxy1):
            sql = 'insert ignore into http_proxy(proxy_addr,valid,source_site,created_time) values("{proxy}",0,"{source_site}",now())'.format(
                proxy=proxy1,source_site=source)
            print(sql)
            db.execute(sql)


if __name__ == '__main__':
    refresh(crawlApi.freeProxy1(proxy_number=1),'www.66ip.cn')
    refresh(crawlApi.freeProxy2(proxy_number=1),'www.youdaili.net')
    refresh(crawlApi.freeProxy3(proxy_number=1),'www.xicidaili.com')
