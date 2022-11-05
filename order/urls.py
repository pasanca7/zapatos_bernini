from django.urls import path
from . import views

urlpatterns = [
    path('line/all/', views.lineList, name="shoe-list"),
    path('line/<int:pk>/', views.lineDetail, name="shoe-detail"),
    path('line/', views.lineCreate, name="shoe-create"),
    path('line/update/<int:pk>', views.lineUpdate, name="shoe-update"),

]