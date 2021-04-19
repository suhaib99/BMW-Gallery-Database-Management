from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.db.models.functions import *
from django.db.models.expressions import RawSQL
from django.db.models import * 
from django.db import connection

# Create your views here.

class CustomerDetail(APIView):
    def get(self, request, pk, format=None):
        customer = Customer.objects.get (pk=pk)
        serializer = CustomerSerializer(customer)
        return Response (serializer.data)

    def delete(self, request, pk, format=None):
        customer = Customer.objects.filter(pk=pk)
        customer.delete() 
        return Response (status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        customer = Customer.objects.filter(pk=pk).first()
        serializer = CustomerSerializer (customer, data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomerList(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer (customers, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(APIView):
    def get(self, request, pk, format=None):
        car = Car.objects.get (pk=pk)
        serializer = CarSerializer(car)
        return Response (serializer.data)

    def delete(self, request, pk, format=None):
        car = Car.objects.filter(pk=pk)
        car.delete() 
        return Response (status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        car = Car.objects.filter(pk=pk).first()
        serializer = CarSerializer (car, data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarList(APIView):
    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = CarSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeList(APIView):
    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get(self, request, pk, format=None):
        employee = Employee.objects.get (pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response (serializer.data)

    def delete(self, request, pk, format=None):
        employee = Employee.objects.filter(pk=pk)
        employee.delete() 
        return Response (status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        employee = Employee.objects.filter(pk=pk).first()
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ThreeMFilmList(APIView):
    def get(self, request, format=None):
        threemfilms = ThreeMFilm.objects.all()
        serializer = ThreeMFilmSerializer(threemfilms, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ThreeMFilmSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ThreeMFilmDetail(APIView):
    def get(self, request, pk, format=None):
        threemfilm = ThreeMFilm.objects.get(pk=pk)
        serializer = ThreeMFilmSerializer(threemfilm)
        return Response (serializer.data)

    def delete(self, request, pk, format=None):
        threemfilm = ThreeMFilm.objects.filter(pk=pk)
        threemfilm.delete() 
        return Response (status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        threemfilm = ThreeMFilm.objects.filter(pk=pk).first()
        serializer = ThreeMFilmSerializer(threemfilm, data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceList(APIView):
    def get(self, request, format=None):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceDetail(APIView):
    def get(self, request, pk, format=None):
        service = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(service)
        return Response (serializer.data)

    def delete(self, request, pk, format=None):
        service = Service.objects.filter(pk=pk)
        service.delete() 
        return Response (status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        service = Service.objects.filter(pk=pk).first()
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ROList(APIView):
    def get(self, request, format=None):
        orders = RepairOrder.objects.all()
        serializer = ROSerializer(orders, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ROSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RODetail(APIView):
    def get(self, request, pk, format=None):
        order = RepairOrder.objects.get(pk=pk)
        serializer = ROSerializer(order)
        return Response (serializer.data)

    def delete(self, request, pk, format=None):
        order = RepairOrder.objects.filter(pk=pk)
        order.delete() 
        return Response (status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        order = RepairOrder.objects.filter(pk=pk).first()
        serializer = ROSerializer(order, data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
class WorksOnList(APIView):
    def get(self, request, format=None):
        works = WorksOn.objects.all()
        serializer = WorksOnSerializer(works, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = WorksOnSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
''' 
class ReqList(APIView):
    def get(self, request, format=None):
        requests = Req.objects.all()
        serializer = ReqSerializer(requests, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ReqSerializer(data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReqDetail(APIView):
    def get(self, request, pk, format=None):
        req = Req.objects.get(pk=pk)
        serializer = ReqSerializer(req)
        return Response (serializer.data)

    def delete(self, request, pk, format=None):
        req = Req.objects.filter(pk=pk)
        req.delete() 
        return Response (status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        req = Req.objects.filter(pk=pk).first()
        serializer = ReqSerializer(req, data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#  ---------------------------------QUERY VIEWS ----------------------------- #      

class CustCars(APIView):
    def get(self, request):
        with connection.cursor() as cursor: 
            cursor.callproc('CustomerCars')
            columns = cursor.description
            data = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        return Response(data, status=status.HTTP_200_OK)

class OrdersByCust(APIView):
    def get(self, request):
        with connection.cursor() as cursor: 
            cursor.callproc('OrdersByCust')
            columns = cursor.description
            data = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        return Response(data, status=status.HTTP_200_OK)

class Markups(APIView):
    def get(self, request):
        with connection.cursor() as cursor: 
            cursor.callproc('Markups')
            columns = cursor.description
            data = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        return Response(data, status=status.HTTP_200_OK) 

class GetCarsByCustomer(APIView):
    def get(self, request, value):
        with connection.cursor() as cursor: 
            cursor.callproc('GetCarsByCustomer', [value])
            columns = cursor.description
            data = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        return Response(data, status=status.HTTP_200_OK) 

class GetOrdersByCar (APIView):
    def get(self, request, value):
        with connection.cursor() as cursor: 
            cursor.callproc('GetOrdersByCar', [value])
            columns = cursor.description
            data = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        return Response(data, status=status.HTTP_200_OK)

class GetMarkupByService (APIView):
    def get(self, request, value):
        with connection.cursor() as cursor: 
            cursor.callproc('GetMarkupByService', [value])
            columns = cursor.description
            data = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        return Response(data, status=status.HTTP_200_OK)

class sortRONew (APIView):
    def get(self, request):
        with connection.cursor() as cursor: 
            cursor.callproc('SortROByDate')
            columns = cursor.description
            data = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        return Response(data, status=status.HTTP_200_OK)

class getROByDate (APIView):
    def get(self, request, value):
        with connection.cursor() as cursor: 
            cursor.callproc('GetROByDate', [value])
            columns = cursor.description
            data = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        return Response(data, status=status.HTTP_200_OK)

class getROByYear (APIView):
    def get(self, request, value):
        with connection.cursor() as cursor: 
            cursor.callproc('GetROByYear', [value])
            columns = cursor.description
            data = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        return Response(data, status=status.HTTP_200_OK)

class getROByEmployee (APIView):
    def get(self, request, value):
        with connection.cursor() as cursor: 
            cursor.callproc('RepairByEmployee', [value])
            columns = cursor.description
            data = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        return Response(data, status=status.HTTP_200_OK)
"""   
with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM customers, cars WHERE customers.CustID = cars.CustID")
        row = cursor.fetchall()
        return row 
        
    def get(self, request, custID, format=None):
        orders = RepairOrder.objects.filter(CustID=custID)
        serializer = ROSerializer(orders)
        return Response(serializer.data)
    """