PRAGMA foreign_keys = off;

DROP TABLE IF EXISTS courseCatalog;
CREATE TABLE IF NOT EXISTS courseCatalog(
    `CRN`  INT PRIMARY KEY,
	`courseNum` INT,
    `subject` varchar(100) NOT NULL,
	`title` varchar(30) NOT NULL,
    `credits` INT NOT NULL,
    `prereq1` INT, 
    `prereq2` INT
	
);


DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(
	`UID` INTEGER PRIMARY KEY DESC,
    `email` varchar(100) NOT NULL,
	`password` varchar(30) NOT NULL,
    `role` varchar(30) NOT NULL, 
    `program` varchar(100),
    `firstname` varchar(30) NOT NULL, 
    `lastname` varchar(30) NOT NULL
	
);

DROP TABLE IF EXISTS classes;
CREATE TABLE IF NOT EXISTS classes(
	`CRN` INTEGER PRIMARY KEY,
    `UID` INTEGER NOT NULL,
    `Subject` varchar(100) NOT NULL,
	`courseNum` varchar(30) NOT NULL,
    `Title` varchar(100) NOT NULL,
    `Credits` INTEGER NOT NULL,
    `Term` varchar(100) NOT NULL,
    `Year` varchar(100) NOT NULL
    
);


DROP TABLE IF EXISTS list_students;
CREATE TABLE IF NOT EXISTS list_students(
    `ID` INTEGER PRIMARY KEY AUTOINCREMENT,
    `firstname` varchar(30) NOT NULL, 
    `lastname` varchar(30) NOT NULL, 
    `UID` INTEGER NOT NULL,
    `Subject` varchar(100) NOT NULL,
	`courseNum` INTEGER NOT NULL,
    `Title` varchar(100) NOT NULL,
    `Term` varchar(100) NOT NULL,
    `Year` varchar(100) NOT NULL,
    `Grade` varchar(30) NOT NULL,
    `CRN` INTEGER NOT NULL
);

DROP TABLE IF EXISTS my_Courses;
CREATE TABLE IF NOT EXISTS my_Courses(
	`ID` INTEGER PRIMARY KEY,
    `CRN` INTEGER NOT NULL,
	`UID` INTEGER NOT NULL,
    `Subject` varchar(100) NOT NULL,
	`courseNum` INTEGER NOT NULL,
    `Title` varchar(100) NOT NULL,
    `Credits` INTEGER NOT NULL,
    `Term` varchar(100) NOT NULL,
    `Year` varchar(100) NOT NULL,
    `Grade` varchar(30) 	
);



INSERT INTO users (UID,email, password, role, program, firstname, lastname) VALUES
('12345678' ,'jdoe@travel.edu','test','student','Masters','John','Doe');
INSERT INTO users (UID,email, password, role, firstname, lastname) VALUES
('12345679' ,'tWood@travel.edu','test','falculty','Tim','Wood');

INSERT INTO users (UID,email, password, role, firstname, lastname) VALUES
('12345680' ,'erice@travel.edu','test','falculty','Emma','Rice');
-- INSERT INTO courseCatalog (courseNum, subject, title, credits) VALUES
-- (123456,6221,'CSCI','SW Paradigms',3);
-- INSERT INTO courseCatalog (courseNum, subject, title, credits) VALUES
-- (12345,6461,'CSCI','Computer Architecture',3);
-- INSERT INTO courseCatalog (courseNum, subject, title, credits) VALUES
-- ( 123458, 6212,'CSCI','Algorithms',3);
-- INSERT INTO courseCatalog (courseNum, subject, title, credits) VALUES
-- (294850, 6220,'CSCI','Machine Learning',3);
-- INSERT INTO courseCatalog (courseNum, subject, title, credits) VALUES
-- ( 9807890, 6232,'CSCI','Networks 1',3);

INSERT INTO courseCatalog (CRN, courseNum, subject, title, credits, prereq1) VALUES
(634569, '6233','CSCI','Networks 2',3, 1111);

INSERT INTO courseCatalog (CRN, courseNum, subject, title, credits) VALUES
(634568,'2441W','CSCI','Databases', 4);

-- INSERT INTO my_Courses (CRN, UID,subject, courseNum, Title, Credits, Term, Year, Grade) VALUES
-- (634568, 12345678,'CSCI', '2441W','Databases', 4, 'Sring', '2020', "IP");


INSERT INTO classes (UID,subject, courseNum, Title, Credits, Term, Year) VALUES
(12345679,'CSCI', '2441W','Databases', 4, 'Sring', '2020');

INSERT INTO classes (CRN, UID,subject, courseNum, Title, Credits, Term, Year) VALUES
(634569,12345680,'CSCI', '6233', 'Networks 2', 3, 'Spring', '2020');

INSERT INTO list_students (firstname, lastname, UID, Subject, courseNum, Title, Term, Year, Grade, CRN) VALUES
("John", "Doe", 12345678,'CSCI', '2441W','Databases','Sring', '2020', "IP", 634568);

PRAGMA foreign_keys = on;


