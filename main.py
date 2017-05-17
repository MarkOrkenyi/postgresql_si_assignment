import sql_queries
import psycopg2
try:
    connect_str = "dbname='markorkenyi' user='markorkenyi' host='localhost' password='shadow123'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
except:
    print("I am unable to connect to the database")
cur = conn.cursor()
sql_queries.question7(cur)
conn.close()
