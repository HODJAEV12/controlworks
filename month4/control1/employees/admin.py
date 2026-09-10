from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = (
        "id", "first_name", "last_name",
        "position", "salary", "created_at" 
    )