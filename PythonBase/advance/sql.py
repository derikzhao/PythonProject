# encoding:UTF-8
import MySQLdb

# 数据库连接
db = MySQLdb.connect("localhost", "root", "sa12345", "taix", charset='utf8')

print(db)

cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(data)

sql = """SELECT * FROM track limit 10 """

cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()

for row in results:
    print row

# 关闭数据库连接
db.close()
