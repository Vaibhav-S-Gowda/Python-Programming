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
cur.execute("INSERT INTO students_1(srn, student_name, semester, section) VALUES(1001, 'Shannu', 'Sem 1', 'D')")
cur.execute("INSERT INTO students_1(srn, student_name, semester, section) VALUES(1002, 'Nypunya', 'Sem 1', 'E')")
cur.execute("INSERT INTO students_1(srn, student_name, semester, section) VALUES(1003, 'Hrithika', 'Sem 1', 'E')")
cur.execute("INSERT INTO students_1(srn, student_name, semester, section) VALUES(1004, 'ELECTRA', 'Sem 1', 'A')")
conn.commit()
cur.close()
conn.close()