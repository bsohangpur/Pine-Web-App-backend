from django.db import models


class Appointment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    street = models.TextField()
    line = models.TextField()
    email = models.EmailField()
    department = models.CharField(max_length=255)
    procedure = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"
