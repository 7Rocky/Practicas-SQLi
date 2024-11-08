DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS professors;

CREATE TABLE IF NOT EXISTS grades (
  student_id INTEGER,
  name TEXT NOT NULL,
  subject TEXT NOT NULL,
  grade TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS professors (
  id INTEGER PRIMARY KEY,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
);

INSERT INTO professors (username, password) VALUES 
('Rocky', 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f');

INSERT INTO grades (student_id, name, subject, grade) VALUES 
(1, 'Alice', 'Math', 'A'),
(1, 'Alice', 'Science', 'B'),
(1, 'Alice', 'English', 'A'),
(2, 'Bob', 'Math', 'C'),
(2, 'Bob', 'Science', 'A'),
(2, 'Bob', 'English', 'B'),
(3, 'Charlie', 'Math', 'B'),
(3, 'Charlie', 'Science', 'C'),
(3, 'Charlie', 'English', 'C'),
(4, 'Daisy', 'Math', 'A'),
(4, 'Daisy', 'Science', 'A'),
(4, 'Daisy', 'English', 'A'),
(5, 'Ethan', 'Math', 'B'),
(5, 'Ethan', 'Science', 'B'),
(5, 'Ethan', 'English', 'C'),
(6, 'Fiona', 'Math', 'C'),
(6, 'Fiona', 'Science', 'C'),
(6, 'Fiona', 'English', 'B'),
(7, 'George', 'Math', 'A'),
(7, 'George', 'Science', 'A'),
(7, 'George', 'English', 'B'),
(8, 'Hannah', 'Math', 'B'),
(8, 'Hannah', 'Science', 'B'),
(8, 'Hannah', 'English', 'C'),
(9, 'Ivan', 'Math', 'C'),
(9, 'Ivan', 'Science', 'A'),
(9, 'Ivan', 'English', 'B'),
(10, 'Julia', 'Math', 'A'),
(10, 'Julia', 'Science', 'A'),
(10, 'Julia', 'English', 'A');
