from dotenv import load_dotenv
load_dotenv()

import pymysql

conn = pymysql.connect(
    user='root', 
    passwd='db_pw', 
    host='127.0.0.1', 
    db= 'open_source', 
    charset='utf8'
)

