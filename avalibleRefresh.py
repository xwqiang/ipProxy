import crawlApi
import util

import db


def refreshAvalible():
    sql = 'select proxy_addr from http_proxy where valid = 0 or valid = 1'
    for row in db.query(sql):
        addr = row.get('proxy_addr')
        valid = 1 if util.validUsefulProxy(addr) else 2
        updateSql = 'update http_proxy set valid = {valid} ,modified_time = now() where proxy_addr = "{proxy_addr}" '.format(
            proxy_addr=addr, valid=valid)
        db.execute(updateSql)


if __name__ == '__main__':
    refreshAvalible()
