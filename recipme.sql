/***************** CREATE DATA-BASE *********************/

DROP DATABASE IF EXISTS `recipme`;

CREATE DATABASE `recipme`;

USE `recipme`;

CREATE TABLE `User`
(
    `UserId` INT NOT NULL AUTO_INCREMENT,
    `Username` NVARCHAR(160) NOT NULL,
    `First` NVARCHAR(30) NOT NULL,
    `Last` NVARCHAR(30) NOT NULL,
    CONSTRAINT `PK_User` PRIMARY KEY  (`UserId`)
);

SHOW TABLES;

DESC USER;
