ALTER TABLE students RENAME COLUMN student_id TO st_id;
ALTER TABLE interests RENAME COLUMN interests TO interest;
ALTER TABLE students ALTER COLUMN st_name TYPE VARCHAR(20);
ALTER TABLE students ALTER COLUMN st_last TYPE VARCHAR(20);
DROP TABLE interests CASCADE;
CREATE TABLE interests(
    student_id INT NOT NULL, 
    interest VARCHAR(20), 
    CONSTRAINT fk FOREIGN KEY (student_id) REFERENCES students(st_id) ON DELETE CASCADE
);
INSERT INTO interests VALUES 
    (1, 'Tennis'), 
    (1, 'Literature'), 
    (2, 'Math'), 
    (2, 'Tennis'), 
    (3, 'Math'), 
    (3, 'Music'), 
    (2, 'Football'), 
    (1, 'Chemistry'), 
    (3, 'Chess');