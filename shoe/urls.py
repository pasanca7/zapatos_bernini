from django.urls import path
from . import views

urlpatterns = [
    path('shoe/all', views.shoeList, name="shoe-list"),
    path('shoe/<str:pk>', views.shoeDetail, name="shoe-detail"),
    path('shoe/', views.shoeCreate, name="shoe-create"),
    path('shoe/update/<str:pk>/', views.shoeUpdate, name="shoe-update"),
    path('shoe/delete/<str:pk>/', views.shoeDelete, name="shoe-delete"),
]