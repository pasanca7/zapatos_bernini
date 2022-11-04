from django.contrib import admin
from shoe.models import Shoe

@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "size", "currency"]