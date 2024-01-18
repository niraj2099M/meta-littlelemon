from django.db import models

# Create your models here.

class booking_table(models.Model):
    name=models.CharField(max_length=255)
    number_of_guests=models.IntegerField()
    booking_date=models.DateTimeField()


class menu_table(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    inventory=models.IntegerField()
