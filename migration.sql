ALTER TABLE students RENAME COLUMN st_id TO student_id;
ALTER TABLE interests RENAME COLUMN interest TO interests;
ALTER TABLE students ALTER COLUMN st_name TYPE VARCHAR(30);
ALTER TABLE students ALTER COLUMN st_last TYPE VARCHAR(30);
DROP TABLE interests CASCADE;
CREATE TABLE interests(
    student_id INT NOT NULL, 
    interests TEXT [], 
    CONSTRAINT fk FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);
INSERT INTO interests(student_id, interests) VALUES (1, '{Tennis,Literature,Chemistry}');
INSERT INTO interests(student_id, interests) VALUES (2, '{Math,Tennis,Football}');
INSERT INTO interests(student_id, interests) VALUES (3, '{Math,Music,Chess}');