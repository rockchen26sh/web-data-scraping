import pymysql

conn = pymysql.connect(host = '127.0.0.1',user = 'root', passwd = '28488747' )
cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
