import sqlalchemy as db

# Create the connection to a particular database
engine = db.create_engine(
    "postgresql://postgres:vaibhavhinduja@localhost:5432/College"
)
# First Value - DataBase software
# Second Value - Username
# Third Value - Password
# Fourth Value - Address of Database
# Fifth Value - Port Number
# Sixth Value - Name of the existing database

print(engine)

# Connect to the Database

with engine.connect() as conn:
    result = conn.execute(db.text("SELECT * FROM students_1"))
    print(type(result))
    print(result)
    print(result.fetchall())

    for r in result.fetchall():
        print(r)