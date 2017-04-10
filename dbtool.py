#: -*- coding: utf-8 -*-
"""
    database
    ~~~~~~~~

    python对mysql操作的封装类
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: rsj217
    :license: BSD.
    :contact: rsj217@gmail.com

    :version: 0.0.1
"""

try:  # 连接 MySQLdb, 或者 pymysql
    import MySQLdb as mysql
except ImportError:
    import pymysql as mysql


class DataBase(object):
    """
        数据库操作类
    """

    def __init__(self, host, user, passwd, database, port=3306, charset='utf8'):
        """初始化数据库配置信息，端口默认 3306 编码 utf-8
        """
        #: * 数据库主机地址
        self.host = host
        #: * 数据库用户名
        self.user = user
        #: * 数据库用户密码
        self.passwd = passwd
        #: * 数据库名
        self.database = database
        #: * 数据库端口
        self.port = port
        #: * 数据库字符编码
        self.charset = charset

    def __get_db(self):
        """链接数据库，获取数据库句柄"""
        #: 数据库连接， 返回资源句柄
        db = mysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            db=self.database,
            port=self.port,
            charset=self.charset)
        return db

    def execrone(self, func):
        '''
            读取数据库，返回单条记录

            parameters
              func
                函数类型,被装饰器包装的函数，不用显示传递

            return
                查询数据库单条记录结果和影响行数


            sample::

                @self.execrone
                def getone():
                    pass

                getone 将会被本方法包装
        '''

        def wrap(*args):
            try:
                #: 连接数据库
                db = self.__get_db()
                #: 获取数据查询游标
                cursor = db.cursor()
                #: 得到 sql 语句
                sql = func(*args)
                #: 执行单条 sql 语句， 返回受影响的行数
                rownum = cursor.execute(sql)
                #: 执行查询，返回单条数据
                result = cursor.fetchone()
                #: 返回查询结果和影响行数
                return (rownum, result)
            except mysql.Error as e:
                print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
            finally:
                #: 关闭游标
                cursor.close()
                #: 关闭数据库
                db.close()

        return wrap

    def execrall(self, func):
        '''
            读取数据库，返回多条记录

            parameters:
              func
                函数类型,被装饰器包装的函数，不用显示传递

            return:
                查询数据库多条记录结果和影响行数

            sample::

                @self.execrall
                def getall():
                    pass
                getall 将会被本方法包装
        '''

        def wrap(*args):
            try:
                #: 连接数据库
                db = self.__get_db()
                #: 获取数据查询游标
                cursor = db.cursor()
                #: 得到 sql 语句
                sql = func(*args)
                #: 执行单条 sql 语句， 返回受影响的行数
                rownum = cursor.execute(sql)
                #: 执行查询，返回多条数据
                result = cursor.fetchall()
                #: 返回查询结果和影响行数
                return (rownum, result)
            except mysql.Error as e:
                print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
            finally:
                #: 关闭游标
                cursor.close()
                #: 关闭数据库
                db.close()

        return wrap

    def execcud(self, func):
        '''
            添加数据库记录，用于 create update delete 操作，
            如果写入数据库失败，则执行回滚操作。

            parameters:
              func
                函数类型,被装饰器包装的函数，不用显示传递

            return:
                增加更新删除数据库影响的行数

            sample::

                @self.execcud
                def insert():
                    pass
                insert 将会被本方法包装
        '''

        def wrap(*args):
            try:
                #: 连接数据库
                db = self.__get_db()
                #: 获取数据查询游标
                cursor = db.cursor()
                #: 得到 sql 语句
                sql = func(*args)
                #: 执行单条 sql 语句， 返回受影响的行数
                rownum = cursor.execute(sql)
                #: 提交查询
                db.commit()
                #: 返回影响行数
                return rownum
            except mysql.Error as e:
                #: 发生错误时回滚
                db.rollback()
                print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
            finally:
                #: 关闭游标
                cursor.close()
                #: 关闭数据库
                db.close()

        return wrap



if __name__ == '__main__':
    database = DataBase(host='localhost', user='root', passwd='xuwuqiang', database='http_proxy');
