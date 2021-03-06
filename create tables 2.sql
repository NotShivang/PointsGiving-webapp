-- MySQL Script generated by MySQL Workbench
-- Tue Oct 29 17:44:09 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Users` (
  `UserId` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Role` VARCHAR(45) NULL,
  `Password` VARCHAR(45) NULL,
  PRIMARY KEY (`UserId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Time_Periods`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Time_Periods` (
  `TimePeriodId` INT NOT NULL,
  `Description` VARCHAR(45) NULL,
  PRIMARY KEY (`TimePeriodId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Transactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Transactions (
TransactionId INT NOT NULL AUTO_INCREMENT,
SenderId INT,
ReceiverId INT,
TimePeriodId INT,
NumberOfPoints INT,
PRIMARY KEY (TransactionId),
FOREIGN KEY (SenderId) REFERENCES Users(UserId),
FOREIGN KEY (ReceiverId) REFERENCES Users(UserId),
FOREIGN KEY (TimePeriodId) REFERENCES Time_Periods(TimePeriodId)
)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User_Month`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`User_Month` (
  `UserMonthId` INT NOT NULL,
  `UserId` INT NULL,
  `MonthlyReportId` VARCHAR(45) NULL,
  `PointsGiven` INT NULL,
  `PointsReceived` INT NULL,
  `PointsRedeemed` INT NULL,
  `TimePeriodId` INT NULL,
  `PointsToGive` INT NULL,
  PRIMARY KEY (`UserMonthId`),
  CONSTRAINT `UserId`
    FOREIGN KEY (`UserId`)
    REFERENCES `mydb`.`Users` (`UserId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `TimePeriodId`
    FOREIGN KEY (`TimePeriodId`)
    REFERENCES `mydb`.`Time_Periods` (`TimePeriodId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
