SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS courseCatalog CASCADE;
CREATE TABLE IF NOT EXISTS courseCatalog(
    `CRN`  INT  AUTO_INCREMENT PRIMARY KEY,
	`courseNum` INT,
    `subject` varchar(100) NOT NULL,
	`title` varchar(30) NOT NULL,
    `credits` INT NOT NULL,
    `prereq1` INT, 
    `prereq2` INT
	
);


DROP TABLE IF EXISTS student CASCADE;
CREATE TABLE IF NOT EXISTS student(
	`UID` INT AUTO_INCREMENT PRIMARY KEY,
    `email` varchar(100) NOT NULL,
	`password` varchar(30) NOT NULL,
    `program` varchar(100) NOT NULL,
    `firstname` varchar(30) NOT NULL, 
    `lastname` varchar(30) NOT NULL
	
);

CREATE TABLE IF NOT EXISTS my_Courses(
	`ID` INT auto_increment PRIMARY KEY,
	`UID` INT NOT NULL,
    `Subject` varchar(100) NOT NULL,
	`courseNum` INT NOT NULL,
    `Title` varchar(100) NOT NULL,
    `Credits` INT NOT NULL,
    `Term` varchar(100) NOT NULL,
    `Year` varchar(100) NOT NULL,
    `Grade` varchar(30) NOT NULL
	
);
ALTER TABLE student AUTO_INCREMENT = 82925298;
ALTER TABLE courseCatalog AUTO_INCREMENT = 1111111;


INSERT INTO `student` (email, password, program, firstname, lastname) VALUES
( 'jdoe@travel.edu','test','Masters','John','Doe');

INSERT INTO `courseCatalog` (courseNum, subject, title, credits) VALUES
( 6221,'CSCI','SW Paradigms',3);
INSERT INTO `courseCatalog` (courseNum, subject, title, credits) VALUES
( 6461,'CSCI','Computer Architecture',3);
INSERT INTO `courseCatalog` (courseNum, subject, title, credits) VALUES
( 6212,'CSCI','Algorithms',3);
INSERT INTO `courseCatalog` (courseNum, subject, title, credits) VALUES
( 6220,'CSCI','Machine Learning',3);
INSERT INTO `courseCatalog` (courseNum, subject, title, credits) VALUES
( 6232,'CSCI','Networks 1',3);
INSERT INTO `courseCatalog` (courseNum, subject, title, credits, prereq1) VALUES
( 6233,'CSCI','Networks 2',3, 1111115);

INSERT INTO `my_Courses` (UID,subject, courseNum, Title, Credits, Term, Year, Grade) VALUES
(82925298,'CSCI',6232,'Networks 1',3, 'Fall', '2020', 'A');



SET FOREIGN_KEY_CHECKS = 1;