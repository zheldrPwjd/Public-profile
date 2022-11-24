from config.db import conn

def record_fire_gps(fireInfo):
    mydb = conn.cursor()
    queryString = '''
    insert into collect_fire (longitude , latitude , device_id , behave_kind , times) 
    values ({} , {} , {} , {} , now() ) '''.format(fireInfo.x_longitude , fireInfo.y_latitude , fireInfo.device_id , fireInfo.behave_kind)
    mydb.execute(queryString)
    conn.commit()
    mydb.close()
# print(mydb)
