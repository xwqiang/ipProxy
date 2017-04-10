import pymysql

import dbtool

def getConnection():
    return pymysql.connect(host="localhost", user="root",  password="xuwuqiang", database="http_proxy")


def query(sql):
    try:
        db = getConnection()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        results = cursor.fetchall()
    finally:
        db.close()
    return results



def execute(sql):
    try:
        db = getConnection()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        db.rollback()
    finally:
        db.close()
