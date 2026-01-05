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

cur.execute("""
    UPDATE students_1
    SET student_name = 'Nypunya Sathish',
        semester = 'Sem 1',
        section = 'E'
    WHERE srn = 1002
""")

conn.commit()
cur.close()
conn.close()
