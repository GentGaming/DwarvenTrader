import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host
                     user="root",  # username
                     passwd="p2950",  # password
                     db="testDB")  # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()
print(cur)
# Select data from table using SQL query.
cur.execute("SELECT * FROM examples")

# print the first and second columns
for row in cur.fetchall():
    print
    row[0], " ", row[1]
