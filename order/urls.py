from django.urls import path
from . import views

urlpatterns = [
    path('line/all/', views.lineList, name="shoe-list"),
    path('line/<int:pk>/', views.lineDetail, name="shoe-detail"),
    path('line/', views.lineCreate, name="shoe-create"),
    path('line/update/<int:pk>', views.lineUpdate, name="shoe-update"),
    path('line/delete/<int:pk>', views.lineDelete, name="shoe-delete"),
    path('all/', views.orderList, name="order-list"),
    path('<int:pk>/', views.orderDetail, name="order-detail"),
    path('', views.orderCreate, name="order-create"),
]