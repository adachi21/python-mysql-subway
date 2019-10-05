import csv
import pymysql
import os

conn = pymysql.connect(host='localhost', user='root', password='apmsetup',
                       db='test', charset='utf8')
curs = conn.cursor()
print(os.getcwd())
f = open(os.getcwd()+'//지하철정보//data.csv', mode='rt', encoding='utf8')
rdr = csv.reader(f)
for line in rdr:
    sql = 'insert into subway values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    curs.execute(sql, line)
conn.commit()
conn.close()
f.close()


