import pymysql

conn = pymysql.connect(
    user='root', 
    passwd='', 
    host='127.0.0.1', 
    db= 'open_source', 
    charset='utf8'
)

mydb = conn.cursor()

mydb.execute("insert into collect_fire (longitude , latitude , device_id , behave_kind , times) values (32.12345678 , 128.12345678 , 0 , 0 , now() )")

conn.commit()
mydb.close()
print(mydb)

# db 테이블 다시 짜기 