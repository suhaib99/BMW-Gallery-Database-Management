from django.db import models
from datetime import date
# api communicates with multiple technologies using json as input 
# Create your models here.

class Customer(models.Model):
    CustID = models.CharField(db_column="CustID", max_length=100, primary_key=True)
    CustName = models.CharField(db_column="CustName", max_length=100)
    CustPhone = models.CharField(db_column="CustPhone", max_length=100)
    CustAddress = models.TextField(db_column="CustAddress", max_length=100)

    class Meta:
        app_label = 'api'
        db_table= "customer"

    def __str__(self):
        return self.CustID 

class Car(models.Model):
    VNNo = models.CharField(db_column="VNNo", max_length = 17, primary_key=True)
    CustID = models.ForeignKey(Customer, db_column="CustID", null=True, on_delete=models.SET_NULL)
    CarMaker = models.CharField(db_column="CarMaker", max_length = 15)
    CarModel = models.CharField(db_column="CarModel", max_length = 10)
    Year = models.CharField(max_length = 4)

    class Meta:
        app_label = 'api'
        db_table = "car"
    
    def __str__(self):
        return self.VNNo


class Employee(models.Model):
    EmployeeID = models.CharField(db_column="EmployeeID", max_length=10, primary_key=True)
    Name = models.CharField(db_column="Name", max_length=15)
    Phone = models.CharField(db_column="Phone", max_length=10)
    Address = models.TextField(db_column="Address", max_length=30)

    class Meta:
        app_label = 'api'
        db_table = "employee"
    
    def __str__(self):
        return self.EmployeeID 


class ThreeMFilm(models.Model):
    ThreeMFilmType = models.CharField(db_column="ThreeMFilmType", max_length=20, primary_key = True)
    Size = models.IntegerField(db_column="Size")
    Markup = models.IntegerField(db_column="Markup")
    QuantityRemain = models.IntegerField(db_column="QuantityRemain", default=0)

    class Meta:
        app_label = 'api'
        db_table = "threemfilm"
    
    def __str__(self):
        return self.ThreeMFilmType



class Service(models.Model):
    Service_Type = models.CharField(db_column="Service_Type", max_length = 20, primary_key=True)
    Service_Price = models.IntegerField(db_column="Service_Price", default=0)
    ThreeMFilmType = models.ForeignKey(ThreeMFilm, db_column="ThreeMFilmType", null=True, on_delete=models.SET_NULL)

    class Meta:
        app_label = 'api'
        db_table = "service"
        unique_together = ("Service_Type", "Service_Price")
    
    def __str__(self):
        return self.Service_Type
        

class RepairOrder(models.Model):
    RONumber = models.CharField(db_column = "RONumber",  max_length=8, primary_key=True)
    VNNo = models.ForeignKey(Car, db_column = "VNNo"  , null=True, on_delete=models.SET_NULL)
    CustID = models.ForeignKey(Customer, db_column="CustID" , null=True, on_delete=models.SET_NULL)
    EmployeeID = models.ForeignKey(Employee, db_column="EmployeeID", null=True, on_delete=models.SET_NULL)
    Date = models.DateField(db_column="Date")
    ServiceType = models.ForeignKey(Service, db_column = "ServiceType", null=True, on_delete=models.SET_NULL)
    # SPrice = models.ForeignKey(Service, db_column = "ServicePrice", null=True, on_delete=models.SET_NULL)
    HoursWorked = models.IntegerField(db_column="HoursWorked",  default=0)
    FilmUsed = models.IntegerField(db_column="FilmUsed", default=0)

    class Meta:
        app_label = 'api'
        db_table = "repairorder"

    def __str__(self):
        return self.RONumber  

'''
class WorksOn(models.Model):
    WorksOnID = models.CharField(db_column="WorksOnID", max_length=10, primary_key=True)
    EmployeeID = models.ForeignKey(Employee, db_column = "EmployeeID" , null=True, on_delete=models.SET_NULL)
    RONumber = models.ForeignKey(RepairOrder, db_column = "RONumber", null=True, on_delete=models.SET_NULL)
    Hours = models.IntegerField(db_column = "Hours")
    Film_Used = models.IntegerField(db_column = "Film_Used")
    
    class Meta:
        app_label = 'api'
        db_table = "works_on"
        unique_together = ('EmployeeID', 'RONumber')
    
    def __str__(self):
        return self.WorksOnID
'''

class Req(models.Model):
    RequestID = models.CharField(db_column="RequestID" ,max_length=10, primary_key = True)
    EmpID = models.ForeignKey(Employee, db_column="EmpID", null=True, on_delete=models.SET_NULL)
    Roll_size = models.IntegerField(db_column="Roll_size")
    Quantity = models.IntegerField(db_column="Quantity")
    Date = models.DateField(db_column="Date")
    class Meta:
        app_label = 'api'
        db_table = "requests"

    def __str__(self):
        return self.RequestID

