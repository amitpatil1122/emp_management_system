from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    Eid = models.IntegerField(unique=True)
    First_name = models.CharField(max_length=100, null=False)
    Last_name = models.CharField(max_length=100)
    # Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    Dept = models.CharField(max_length=100)
    Salary = models.IntegerField(default=0)
    Bonus = models.IntegerField(default=0)
    # Desg = models.ForeignKey(Designation, on_delete=models.CASCADE)
    Desg = models.CharField(max_length=100)
    Phone = models.IntegerField(default=0)
    DOJ = models.DateField()

    def __str__(self):
        return self.First_name