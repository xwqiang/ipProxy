import pymysql


def getConnection():
    return pymysql.connect(host="localhost", user="root",  password="xuwuqiang", database="http_proxy")


def query(sql):
    db = getConnection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    cursor.commit()
    results = cursor.fetchall()
    db.close()
    return results


def execute(sql):
    db = getConnection()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
