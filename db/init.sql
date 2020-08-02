CREATE DATABASE LoginData;
use LoginData;

DROP TABLE if exists Accounts;

CREATE TABLE IF NOT EXISTS Accounts (
    `id` INT AUTO_INCREMENT,
    `First_Name` VARCHAR(60) NOT NULL,
    `Last_Name` VARCHAR(60) NOT NULL,
    `Email` VARCHAR(100) NOT NULL,
    `Password` VARCHAR(33) NOT NULL,
    `Verified` INT,
    PRIMARY KEY (`id`)
);
INSERT INTO Accounts (First_Name, Last_Name, Email, Password, Verified) VALUES
    ('FN', 'LN', 'EM@gmail.com', 'PW', '1'),
    ('Kelly', 'Blackledge', 'kb8@njit.edu', 'Password', '1');

