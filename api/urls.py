from django.urls import path, include
from . import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view()),
    path('customers/<pk>/', views.CustomerDetail.as_view()),

    path('cars/', views.CarList.as_view()),
    path('cars/<pk>/', views.CarDetail.as_view()),
    
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<pk>/', views.EmployeeDetail.as_view()),
    
    path('threemfilms/', views.ThreeMFilmList.as_view()),
    path('threemfilms/<pk>/', views.ThreeMFilmDetail.as_view()),
    
    path('services/', views.ServiceList.as_view()),
    path('services/<pk>/', views.ServiceDetail.as_view()),

    path('orders/', views.ROList.as_view()),
    path('orders/<pk>/', views.RODetail.as_view()),
    
    # path('works/', views.WorksOnList.as_view()),
    path('requests/', views.ReqList.as_view()),
    path('requests/<pk>/', views.ReqDetail.as_view()),

    #Queries
    # <---- LIST OF CUSTOMERS AND THEIR CARS ----> 
    path('custcars/', views.CustCars.as_view()),
    # <---- LIST OF REPAIR ORDERS AND THE CUSTOMER INFO ASSOCIATED ----> 
    path('ordersbycust/', views.OrdersByCust.as_view()),
    # <---- LIST OF REPAIR ORDERS AND THE CUSTOMER INFO ASSOCIATED ----> 
    path('markups/', views.Markups.as_view()),
    # <---- LIST OF REPAIR ORDERS AND THE CUSTOMER INFO ASSOCIATED ----> 
    path('getcarsbycustomers/<value>/', views.GetCarsByCustomer.as_view()),
    # <---- LIST OF REPAIR ORDERS AND THE CUSTOMER INFO ASSOCIATED ----> 
    path('getordersbycar/<value>/', views.GetOrdersByCar.as_view()),
    # <---- LIST OF REPAIR ORDERS AND THE CUSTOMER INFO ASSOCIATED ----> 
    path('getmarkupbyservice/<value>/', views.GetMarkupByService.as_view()),
    # <---- LIST OF REPAIR ORDERS AND THE CUSTOMER INFO ASSOCIATED ----> 
    path('getROByEmployee/<value>/', views.getROByEmployee.as_view()),
    # <---- LIST OF REPAIR ORDERS AND THE CUSTOMER INFO ASSOCIATED ----> 
    path('sortRONew/', views.sortRONew.as_view()),
    # <---- LIST OF REPAIR ORDERS AND THE CUSTOMER INFO ASSOCIATED ----> 
    path('getROByYear/<value>/', views.getROByYear.as_view()),
    # <---- LIST OF REPAIR ORDERS AND THE CUSTOMER INFO ASSOCIATED ----> 
    path('getROByDate/<value>/', views.getROByDate.as_view())
]