import pymysql

conn = pymysql.connect(host='localhost', user='root', password='apmsetup',
                        db='test', charset='utf8')
curs = conn.cursor()
station=''
line=''
while True:
    station = input('\n역명:')
    if station=='q':
        print('프로그램 종료')
        break

    sql = "select count(*) from subway where station='{0}'".format(station)
    curs.execute(sql)
    row = curs.fetchone()
    if row[0]>0:
        print('검색하신 역은 {0} 입니다.'.format(station))
        sql = "select distinct line from subway where station='{0}' order by line asc".format(station)
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            print(row[0],end=" ")
    else:       
        sql = "select count(distinct station) as cnt from subway where station like '%{0}%'".format(station)
        curs.execute(sql)
        row = curs.fetchone()
        if row[0]==0:
            print('검색결과 없음')
            continue
        elif row[0]==1:
            sql = "select station from subway where station like '%{0}%'".format(station)
            curs.execute(sql)
            row = curs.fetchone()
            print('검색하신 역은 {0} 입니다.'.format(row[0]))
            station=row[0]
            sql = "select distinct line from subway where station ='{0}' order by line asc".format(station)
            curs.execute(sql)
            rows = curs.fetchall()
            for row in rows:
                print(row[0],end=" ")
        else:
            sql = "select distinct station from subway where station like '%{0}%'".format(station)
            curs.execute(sql)
            rows = curs.fetchall()
            for row in rows:
                print(row[0], end="   ")
            print('')
            continue

    while True:
        line = input('\n호선:')

        print('모든정보(1)')
        print('특정시간(2)')
        print('다시검색(3)')
        menu = int(input('입력:'))

        if menu==1:
            sql = "select * from subway where station='{0}' and line='{1}'".format(station,line)
            curs.execute(sql)
            row = curs.fetchone()

            stepA=2
            stepB=3
            for i in range(24):
                if i<20:            
                    print('{0}-{1}시 승차:{2}, 하차:{3}'.format(i+4, i+5, row[i+stepA], row[i+stepB]))
                    stepA+=1
                    stepB+=1
                elif i==20:
                    print('{0}-{1}시 승차:{2}, 하차:{3}'.format(24, 1, row[i+stepA], row[i+stepB]))
                    stepA+=1
                    stepB+=1
                elif i>20:
                    print('{0}-{1}시 승차:{2}, 하차:{3}'.format(i-20, i-19, row[i+stepA], row[i+stepB]))
                    stepA+=1
                    stepB+=1                   
        elif menu==2:
            searchtime = input('시간:')
            inttime = int(searchtime[0:2])

            sql="select i{0} from subway where station='{1}' and line='{2}'".format(inttime, station, line)
            curs.execute(sql)
            row = curs.fetchone()
            print('{0}-{1}시 승차:{2}'.format(inttime, inttime+1, row[0]))
            
            sql="select o{0} from subway where station='{1}' and line='{2}'".format(inttime, station, line)
            curs.execute(sql)
            row = curs.fetchone()
            print('{0}-{1}시 하차:{2}'.format(inttime, inttime+1, row[0]))
        elif menu==3:
            break     