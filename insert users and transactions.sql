INSERT INTO Users Values (1, "Katie", "Admin", "AdminPassword");
INSERT INTO Users Values (2, "Shivang", "Employee", "ShivangPassword");
INSERT INTO Users Values (3, "Shayna", "Employee", "ShaynaPassword");
INSERT INTO Users Values (4, "Caryn", "Employee", "CarynPassword");
INSERT INTO Users Values (5, "Constantine", "Employee", "CPassword");
INSERT INTO Users Values (6, "Anitesh", "Employee", "AniteshPassword");


INSERT INTO Time_Periods Values (1, "September");
INSERT INTO Time_Periods Values (2, "October");
INSERT INTO Time_Periods Values (3, "November");

--send everyone 1000 at beginning of month 
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (1, 2, 1, 1000);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (1, 3, 1, 1000);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (1, 4, 1, 1000);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (1, 5, 1, 1000);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (1, 6, 1, 1000);

--random transactions for month 1
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (2, 4, 1, 200);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (3, 6, 1, 600);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (4, 2, 1, 50);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (5, 3, 1, 750);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (6, 5, 1, 180);

--reset points to give  for month 2
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (1, 2, 2, 1000);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (1, 3, 2, 1000);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (1, 4, 2, 1000);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (1, 5, 2, 1000);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (1, 6, 2, 1000);

--random transactions for month 1
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (2, 5, 2, 220);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (3, 2, 2, 430);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (4, 6, 2, 700);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (5, 4, 2, 100);
INSERT INTO	Transactions(SenderId, ReceiverId, TimePeriodId, NumberOfPoints) Values (6, 3, 2, 650);
