from fund_rank.DBUtil import DBUtil
dbUtil=DBUtil('localhost', 3306, 'root','mysql','test','utf8')
sql="SELECT * from fund_rank f  limit 1 "
dbUtil.getJsonFromSQL(sql)
