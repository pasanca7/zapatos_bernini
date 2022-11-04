from django.urls import path
from . import views

urlpatterns = [
    path('all', views.shoeList, name="shoe-list"),
    path('<str:pk>', views.shoeDetail, name="shoe-detail"),
    path('', views.shoeCreate, name="shoe-create"),
    path('update/<str:pk>/', views.shoeUpdate, name="shoe-update"),
    path('delete/<str:pk>/', views.shoeDelete, name="shoe-delete"),
]