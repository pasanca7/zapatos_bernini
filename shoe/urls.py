from django.urls import path
from . import views

urlpatterns = [
    path('all', views.shoeList, name="shoe-list"),
    path('<int:pk>', views.shoeDetail, name="shoe-detail"),
    path('', views.shoeCreate, name="shoe-create"),
    path('update/<int:pk>/', views.shoeUpdate, name="shoe-update"),
    path('delete/<int:pk>/', views.shoeDelete, name="shoe-delete"),
]