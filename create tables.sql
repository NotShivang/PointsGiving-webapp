CREATE TABLE IF NOT EXISTS `mydb`.`Transactions` (
  `TransactionId` INT NOT NULL,
  `SenderId` INT NULL,
  `ReceiverId` INT NULL,
  `NumberOfPoints` VARCHAR(45) NULL,
  `TimePeriodId` INT NULL,
  PRIMARY KEY (`TransactionId`),
  CONSTRAINT `SenderId`
    FOREIGN KEY (`SenderId`)
    REFERENCES `mydb`.`Users` (`UserId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `TimePeriodId`
    FOREIGN KEY (`TimePeriodId`)
    REFERENCES `mydb`.`Time_Periods` (`TimePeriodId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    )





ENGINE = InnoDB;