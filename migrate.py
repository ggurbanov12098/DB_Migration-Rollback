import psycopg2 as psql # pip install psycopg2

# Connect to PostgreSQL
conn = psql.connect(
    dbname='postgres',
    user='',
    password='hawx',
    host='127.0.0.1',
    port=5432
)
cur = conn.cursor() #cursor

#This method adds the reverse of the executed command to rollback_commands list
def rollback_log_file(command, rollback_command): 
    rollback_command.append(command)
###############################################################################################
    

def renameColumn(cur, rollback_command):
    cur.execute('ALTER TABLE students RENAME COLUMN st_id TO student_id;')
    rollback_log_file('ALTER TABLE students RENAME COLUMN student_id TO st_id;', rollback_command)
    cur.execute('ALTER TABLE interests RENAME COLUMN interest TO interests;')
    rollback_log_file('ALTER TABLE interests RENAME COLUMN interests TO interest;', rollback_command)

def changeLenColumn(cur, rollback_command):
    cur.execute('ALTER TABLE students ALTER COLUMN st_name TYPE VARCHAR(30);')
    rollback_log_file('ALTER TABLE students ALTER COLUMN st_name TYPE VARCHAR(20);', rollback_command)
    cur.execute('ALTER TABLE students ALTER COLUMN st_last TYPE VARCHAR(30);')
    rollback_log_file('ALTER TABLE students ALTER COLUMN st_last TYPE VARCHAR(20);', rollback_command)


def migrateInterests(cur, rollback_command):
    cur.execute('SELECT * FROM interests;')
    temp = cur.fetchall() # variable holds temporarily the retrieved data from the last(old) interests table

    cur.execute('DROP TABLE interests CASCADE;')
    rollback_log_file('DROP TABLE interests CASCADE;', rollback_command)
    cur.execute('CREATE TABLE interests (student_id INT NOT NULL, interests TEXT [], CONSTRAINT fk FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE);')
    rollback_log_file('CREATE TABLE interests (student_id INT NOT NULL, interest VARCHAR(20), CONSTRAINT fk FOREIGN KEY (student_id) REFERENCES students(st_id) ON DELETE CASCADE);', rollback_command)
    

    dict = {} #Dictionary or array of strings to store interests
    for res in temp:
        student_id = res[0] #key represents student_id
        interest_name = res[1] #value is the name of the interest
        if not student_id in dict:
            dict[student_id] = [interest_name] #if student_id does not exist in the dictionary add it
        else:
            dict[student_id].append(interest_name) #if it exists append its list by the interest name
        rollback_log_file("INSERT INTO interests VALUES (%s, '%s');" % (student_id, interest_name), rollback_command)

    #Inserting arrays into the new table
    for student_id, interest_name in dict.items():
        cur.execute("INSERT INTO interests (student_id, interests) VALUES (%s, %s);", (student_id, interest_name))





rollback_command = []
try:
    renameColumn(cur, rollback_command)
    changeLenColumn(cur, rollback_command)
    migrateInterests(cur, rollback_command)
    conn.commit()
    with open("rollback_log.txt","w") as f:
        f.write('\n'.join(rollback_command))
except Exception as e:
    print(str(e))
    print("Migration failed, be sure that you do NOT execute migration process more than once in a row")
