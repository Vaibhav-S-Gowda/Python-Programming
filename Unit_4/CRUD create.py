import psycopg2 as psy

# Connect to the college Database
conn = psy.connect(
    dbname = 'College',
    user = 'postgres',
    password = 'vaibhavhinduja',
    host = 'localhost'
)

if conn:
    print('Connection established successfully.')
else:
    print('Connection to PostgreSQL encountered error.')

# ------------------
# Create the cursor
# ------------------

cur = conn.cursor() # Opening the cursor

# CRUD operation - Create the table
cur.execute(
    """
    CREATE TABLE students_1(
    srn SERIAL PRIMARY KEY,
    student_name VARCHAR(80) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    section VARCHAR(2) NOT NULL);
    """
)

conn.commit() # Commit the changes
conn.close() # Close the connection
