
# import mysql.connector
import pymysql


conn = pymysql.connect(
    user='root', 
    passwd='m8161516', 
    host='127.0.0.1', 
    db= 'open_source', 
    charset='utf8'
)

mydb = conn.cursor() # db 커넥트 
# print(mydb , "db is connected!!")

# file = open('test.csv','r')
# csv_list = csv.reader(file) # csv을 이차원 배열 형식으로 만들어 줌 


# for i in csv_list:
#     x = i[2] 
#     y = i[3] 
#     name = i[1]
#     print(i)
#     queryString = f"insert into test (x,y,name) values ({x} ,{y} , '{name}');"
#     mydb.execute(queryString)
# mydb.execute("insert into test (x,y,name) values (1,2,'한글이 될까요 ?????')")
mydb.execute("insert into collect_fire (longitude , latitude , device_id , behave_kind , times) values (32.12345678 , 128.12345678 , 0 , 0 , now() )")

conn.commit()
mydb.close()
print(mydb)

# db 테이블 다시 짜기 