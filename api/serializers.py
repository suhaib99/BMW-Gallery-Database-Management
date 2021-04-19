from rest_framework import serializers
from . import models

# need to define serializer class:
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class ThreeMFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ThreeMFilm
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'

class ROSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RepairOrder
        fields = '__all__'

'''
class WorksOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorksOn
        fields = '__all__'
''' 
class ReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Req
        fields = '__all__'
