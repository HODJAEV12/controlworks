from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)