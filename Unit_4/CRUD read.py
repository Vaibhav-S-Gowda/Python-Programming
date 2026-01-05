import psycopg2 as psy

# Connect to the college Database
conn = psy.connect(
    dbname = 'College',
    user = 'postgres',
    password = 'vaibhavhinduja',
    host = 'localhost',
    port = '5432'
)

if conn:
    print('Connection established successfully.')
else:
    print('Connection to PostgreSQL encountered error.')

cur = conn.cursor()
cur.execute("SELECT * FROM students_1")
rows = cur.fetchall()
conn.commit()
cur.close()
conn.close()

for row in rows:
    print(row)