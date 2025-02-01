-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema typing
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `typing` ;

-- -----------------------------------------------------
-- Schema typing
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `typing` DEFAULT CHARACTER SET utf8 ;
USE `typing` ;

-- -----------------------------------------------------
-- Table `typing`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `typing`.`User` ;

CREATE TABLE IF NOT EXISTS `typing`.`User` (
  `Id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(45) NOT NULL,
  `FirstName` VARCHAR(45) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `typing`.`Game`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `typing`.`Game` ;

CREATE TABLE IF NOT EXISTS `typing`.`Game` (
  `Id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `WordPerMinute` INT NOT NULL,
  `Accuracy` DECIMAL(5,2) NOT NULL,
  `Level` INT NOT NULL,
  `LivesLeft` INT NOT NULL,
  `User_Id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_Game_User_idx` (`User_Id` ASC) VISIBLE,
  CONSTRAINT `fk_Game_User`
    FOREIGN KEY (`User_Id`)
    REFERENCES `typing`.`User` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- Insert dummy users
INSERT INTO User(Username, FirstName, LastName, Password) VALUES
('john_doe', 'John', 'Doe', 'hashedpassword1'),
('jane_smith', 'Jane', 'Smith', 'hashedpassword2');

-- Insert dummy game records for John Doe (User_Id = 1)
INSERT INTO Game(WordPerMinute, Accuracy, Level, LivesLeft, User_Id) VALUES
(50, 92.50, 1, 3, 1),
(60, 89.75, 2, 2, 1),
(75, 94.30, 3, 1, 1),
(80, 96.00, 4, 2, 1),
(90, 97.50, 5, 1, 1);

-- Insert dummy game records for Jane Smith (User_Id = 2)
INSERT INTO Game(WordPerMinute, Accuracy, Level, LivesLeft, User_Id) VALUES
(45, 88.00, 1, 3, 2),
(55, 91.20, 2, 2, 2),
(70, 93.50, 3, 1, 2),
(85, 95.80, 4, 2, 2),
(95, 98.00, 5, 1, 2);
