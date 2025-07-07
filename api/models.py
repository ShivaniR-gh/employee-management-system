from django.db import models

# Master Tables
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Designation(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class EmployeeType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

# Employee Table
class Employee(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    job_type = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    designation = models.CharField(max_length=100)

    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    employee_type = models.ForeignKey(EmployeeType, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


