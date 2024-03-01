CREATE TABLE IF NOT EXISTS students(
    st_id SERIAL PRIMARY KEY, 
    st_name VARCHAR(20), 
    st_last VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS interests(
    student_id INT NOT NULL, 
    interest VARCHAR(20), 
    CONSTRAINT fk FOREIGN KEY (student_id) REFERENCES students(st_id) ON DELETE CASCADE
);
INSERT INTO students(st_name, st_last) VALUES 
    ('Konul', 'Gurbanova'), 
    ('Shahnur', 'Isgandarli'), 
    ('Natavan', 'Mammadova');
INSERT INTO interests(student_id, interest) VALUES 
    (1, 'Tennis'), 
    (1, 'Literature'), 
    (2, 'Math'), 
    (2, 'Tennis'), 
    (3, 'Math'), 
    (3, 'Music'), 
    (2, 'Football'), 
    (1, 'Chemistry'), 
    (3, 'Chess');