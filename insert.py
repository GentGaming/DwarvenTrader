import MySQLdb
def writeToTable(database,password,table,row,value):
    conn = MySQLdb.connect(host= "localhost",
                      user="root",
                      passwd=password,
                      db=database)
    x = conn.cursor()

    try:
       x.execute("""INSERT INTO table VALUES (row)""",(value))
       conn.commit()
    except:
       conn.rollback()

    conn.close()