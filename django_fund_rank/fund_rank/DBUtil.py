#coding=utf-8
import json

import pymysql


class DBUtil:
    def __init__(self, host,port,user,passwd,db,charset):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.db=db
        self.charset=charset  
    def getJsonFromSQL(self,sql):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd,db=self.db,charset=self.charset)
        cursor =conn.cursor()
        print("sql:"+sql)
        cursor.execute(sql)
        resultList = cursor.fetchall()
        for result in resultList:
            print(result)
            print(json.dumps(result))
        conn.commit()
        cursor.close()
        conn.close()
         
        