CREATE DATABASE LoginData;
use LoginData;

DROP TABLE if exists LoginData;

CREATE TABLE IF NOT EXISTS Accounts (
    `id` INT AUTO_INCREMENT,
    `Username` VARCHAR(33) NOT NULL,
    `Password` VARCHAR(33) NOT NULL,
    `First_Name` VARCHAR(60) NOT NULL,
    `Last_Name` VARCHAR(60) NOT NULL,
    `Email` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`id`)
);
INSERT INTO Accounts (Username, Password, First_Name, Last_Name, Email) VALUES
('test', 'testpw', 'testfn', 'testln', 'testem@test.com');
