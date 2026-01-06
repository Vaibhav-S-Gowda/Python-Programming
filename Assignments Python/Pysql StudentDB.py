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

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS StudentDB(
    srn SERIAL(1003) PRIMARY KEY,
    sname VARCHAR(80) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    marks integer NOT NULL,
    section VARCHAR(2) NOT NULL);
    """
)
# cur.execute("ALTER TABLE StudentDB DROP COLUMN srn;")
# cur.execute("""
#     ALTER TABLE StudentDB
#     ADD COLUMN python INTEGER,
#     ADD COLUMN java INTEGER,
#     ADD COLUMN ds INTEGER,
#     ADD COLUMN osd INTEGER,
#     ADD COLUMN dba INTEGER,
#     ADD COLUMN oose INTEGER;
# """)
# cur.execute("""
# ALTER TABLE StudentDB
# ADD COLUMN srn INTEGER GENERATED ALWAYS AS IDENTITY
#         (START WITH 1000 INCREMENT BY 1)
# """)
# cur.execute("""
#     UPDATE StudentDB
#     SET semester = 'Sem1',
#         section = 'E',
#         python = 85,
#         java   = 98,
#         ds     = 90,
#         osd    = 88,
#         dba    = 92,
#         oose   = 80
#     WHERE srn = 1006;
# """)


def insert_student(cur, conn):
    sname = input("Enter student name: ")
    semester = input("Enter semester (e.g., Sem 1): ")
    section = input("Enter section: ")

    python = int(input("Enter Python marks: "))
    java = int(input("Enter Java marks: "))
    ds = int(input("Enter DS marks: "))
    osd = int(input("Enter OSD marks: "))
    dba = int(input("Enter DBA marks: "))
    oose = int(input("Enter OOSE marks: "))

    cur.execute("""
        INSERT INTO StudentDB (sname, semester, section,python, java, ds, osd, dba, oose)
        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, ( sname, semester, section,
          python, java, ds, osd, dba, oose))

    conn.commit()
    print("Record inserted successfully.")

insert_student(cur, conn)   

conn.commit()
conn.close() # Close the connection
cur.close()
