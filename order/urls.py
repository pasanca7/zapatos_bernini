from django.urls import path
from . import views

urlpatterns = [
    path('line/all/', views.lineList, name="line-list"),
    path('line/<int:pk>/', views.lineDetail, name="line-detail"),
    path('line/', views.lineCreate, name="line-create"),
    path('line/update/<int:pk>', views.lineUpdate, name="line-update"),
    path('line/delete/<int:pk>', views.lineDelete, name="line-delete"),
    path('all/', views.orderList, name="order-list"),
    path('<int:pk>/', views.orderDetail, name="order-detail"),
    path('', views.orderCreate, name="order-create"),
]