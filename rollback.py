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

##################################################################

def rollback(cur, rollback_command):
    for command in rollback_command:
        cur.execute(command)        
        
try:
    rollback(cur, open("rollback_log.txt").read().split("\n"))
    conn.commit()
except Exception as e:
    print(str(e))
    print("Rollback failed")

conn.commit()