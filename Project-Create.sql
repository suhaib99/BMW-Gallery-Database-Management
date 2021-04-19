/* TABLE CREATION */ 

CREATE TABLE customer
		(CustID			CHAR(8)		NOT NULL,
		CustName		VARCHAR(15)		NOT NULL,
		CustPhone		CHAR(10)		NOT NULL, 
		CustAddress		VARCHAR(30)		NOT NULL, 
		PRIMARY KEY (CustID));
        
CREATE TABLE car
		(VNNo			CHAR(12)		NOT NULL,
		CustID			CHAR(8)			NOT NULL,
		CarMaker		VARCHAR(15)		NOT NULL,
        CarModel		VARCHAR(15)		NOT NULL,
		Year			CHAR(9)			NOT NULL, 
		PRIMARY KEY (VN_No),
		FOREIGN KEY (CustID) REFERENCES customer (CustID) );
		
CREATE TABLE employee
		(EmployeeID		CHAR(10)			NOT NULL,
		Name			VARCHAR(15)		NOT NULL,
		Phone			CHAR(10)		NOT NULL, 
		Address			VARCHAR(30)		NOT NULL,
		PRIMARY KEY (EmployeeID),
		unique (EmployeeID));
        
CREATE TABLE threemfilm
		(ThreeMFilmType	VARCHAR(20)		NOT NULL,
		Size			int				NOT NULL,
		Markup			int				NOT NULL,
		RollSize		int				NOT NULL, 
		unique (ThreeMFilmType));
        
CREATE TABLE service
		(Service_Type	VARCHAR(8)		NOT NULL,
		Service_Price	int				NOT NULL,
		ThreeMFilmType	VARCHAR(20)		NOT NULL,
		unique (Service_Type),
		FOREIGN KEY (ThreeMFilmType) REFERENCES ThreeMFilm(ThreeMFilmType));

CREATE TABLE repair_order
		(RONumber		CHAR(8)			NOT NULL,
		VNNo			CHAR(12)		NOT NULL,
		CustID			CHAR(8)			NOT NULL,
		EmployeeID		CHAR(10)			NOT NULL, 
		Date			date			NOT NULL, 
		ServiceType		VARCHAR(20)		NOT NULL, 
		ServicePrice	int				NOT NULL, 
		PRIMARY KEY (RO_Number),
		FOREIGN KEY (CustID) REFERENCES customer(CustID),
		FOREIGN KEY (VN_No) REFERENCES car(VN_No),
		FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID));
   
CREATE TABLE works_on
		(WorksOnID		VARCHAR(10)		NOT NULL,
        EmployeeID		CHAR(10)		NOT NULL,
		RONumber		CHAR(8)			NOT NULL,
		Hours			int				NOT NULL,
		Film_Used		int				NOT NULL, 
		FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID),
		FOREIGN KEY (RO_Number) REFERENCES repair_order(RO_Number));
	
CREATE TABLE requests
		(RequestID		VARCHAR(10)			NOT NULL,
        EmpID			CHAR(10)			NOT NULL,
		Roll_size 		int				NOT NULL,
		Quantity		int				NOT NULL,
		Date			date			NOT NULL,  
        PRIMARY KEY (RequestID), 
		FOREIGN KEY (EmployeeID) REFERENCES employee(EmployeeID));

/* PROCEDURE CREATION */ 
DELIMITER 
CREATE DEFINER=`root`@`localhost` PROCEDURE `CustomerCars`()
BEGIN
	SELECT customer.CustID, customer.CustName, car.CarMaker, car.CarModel, car.Year
	FROM customer   
    INNER JOIN car
    ON customer.CustID=car.CustID; 
END; 
END; 
DELIMITER; 

DELIMITER
CREATE DEFINER=`root`@`localhost` PROCEDURE `Markups`()
BEGIN
	SELECT service.Service_Type, threemfilm.Size, threemfilm.Markup 
	FROM threemfilm, service
	WHERE service.ThreeMFilmType = threemfilm.ThreeMFilmType
	GROUP BY service.Service_Type;
END;
DELIMITER; 

CREATE DEFINER=`root`@`localhost` PROCEDURE `OrdersByCust`()
BEGIN
	SELECT repairorder.RONumber, repairorder.VNNo, customer.CustID
	FROM repairorder  
    INNER JOIN customer
    ON repairorder.CustID=customer.CustID; 
END; 

CREATE DEFINER=`root`@`localhost` PROCEDURE `GetCarsByCustomer`(
	IN inputID VARCHAR(10)
)
BEGIN
	SELECT inputID, CustName, VNNo, CarMaker, CarModel, Year
	FROM customer
	CROSS JOIN car
    WHERE inputID = car.CustID and inputID = customer.CustID;
END

CREATE DEFINER=`root`@`localhost` PROCEDURE `GetOrdersByCar`(
	IN inputVN CHAR(12)
)
BEGIN
	SELECT RONumber, car.VNNo, repairorder.CustID, car.CarMaker, car.CarModel, car.Year, repairorder.ServiceType
	FROM car
	CROSS JOIN repairorder
    WHERE inputVN = car.VNNo and inputVN = repairorder.VNNo;
END

CREATE DEFINER=`root`@`localhost` PROCEDURE `RepairByEmployee`(
	IN inputID CHAR(8)
)
BEGIN
	SELECT inputID, RONumber, repairorder.VNNo, repairorder.Date, repairorder.HoursWorked
	FROM employee
	CROSS JOIN repairorder
    WHERE inputID = repairorder.EmployeeID and inputID = employee.EmployeeID;
END
 
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetMarkupByService`(
	IN inputServiceType VARCHAR(15)
)
BEGIN
	SELECT inputServiceType, threemfilm.ThreeMFilmType, threemfilm.Markup, threemfilm.QuantityRemain
	FROM service
	CROSS JOIN threemfilm
    WHERE inputServiceType = service.Service_Type and service.ThreeMFilmType = threemfilm.ThreeMFilmType;
END

CREATE DEFINER=`root`@`localhost` PROCEDURE `GetRObyDate`(
    IN inputDate datetime
)
BEGIN
	SELECT *
    FROM repairorder
    WHERE Date = inputDate 
    ORDER BY inputDate; 
END

CREATE DEFINER=`root`@`localhost` PROCEDURE `SortROByDate`()
BEGIN
	SELECT *
    FROM repairorder
    Order by date ASC; 
END
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetRObyYear`(
    IN inputYear char(4)
)
BEGIN
	SELECT *
    FROM repairorder
    WHERE year(Date) = inputYear 
    ORDER BY inputDate; 
END