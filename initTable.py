import psycopg2 as psql # pip install psycopg2

# Database connection parameters
DB_NAME = 'postgres'
DB_USER = ''
DB_PASSWORD = 'hawx'
DB_HOST = '127.0.0.1'
DB_PORT = 5432

# Connect to PostgreSQL
conn = psql.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cur = conn.cursor()

#This method adds the reverse of the executed command to rollback_commands list
def rollback_log_file(command, rollback_command):
    rollback_command.append(command)

####################################################################################
    
# SQL queries for table creation
create_tables = [
    """
    CREATE TABLE IF NOT EXISTS students (
        st_id SERIAL PRIMARY KEY,
        st_name VARCHAR(20),
        st_last VARCHAR(20)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS interests (
        --interests_id SERIAL PRIMARY KEY,
        student_id INT NOT NULL,
        interest VARCHAR(20),
        CONSTRAINT fk FOREIGN KEY (student_id) REFERENCES students(st_id) ON DELETE CASCADE
    );
    """
]

def createTables():
    for query in create_tables:
        cur.execute(query)
        conn.commit()

createTables()

# SQL queries for sample data insertion
insert_data = [
    """
    INSERT INTO students (st_name, st_last) VALUES
    ('Konul', 'Gurbanova'),
    ('Shahnur', 'Isgandarli'),
    ('Natavan', 'Mammadova');
    """,
    """
    INSERT INTO interests (student_id, interest) VALUES
    (1, 'Tennis'),
    (1, 'Literature'),
    (2, 'Math'),
    (2, 'Tennis'),
    (3, 'Math'),
    (3, 'Music'),
    (2, 'Football'),
    (1, 'Chemistry'),
    (3, 'Chess');
    """
]

def insertData():
    for query in insert_data:
        cur.execute(query)
        conn.commit()

insertData()