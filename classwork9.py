import sqlite3
connection = sqlite3.connect("itsteps_DB.sl3", 5)
cur = connection.cursor()
# print(connection)
# print(cur)
# cur.execute("CREATE TABLE first_tables (name TEXT, age INT);")
cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
cur.execute("INSERT INTO first_table (name) VALUES ('Vova');")
cur.execute("INSERT INTO first_table (name) VALUES ('Max');")
cur.execute("SELECT rowid, name FROM first_table;")
# cur.execute("SELECT rowid, name FROM first_tables WHERE name=("Anna");")
cur.execute("UPDATE first_table SET name='Andrew' WHERE name = ('Max');")
cur.execute("SELECT rowid, name FROM first_table;")


cur.execute("DELETE FROM first_table WHERE rowid>5 AND rowid<10;")
cur.execute("SELECT rowid, name FROM first_table;")

res = cur.fetchall()
print(res)
connection.commit()
connection.close()