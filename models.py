from django.db import models
class user(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


class address(models.Model):
    pincode = models.IntegerField(max_length=10)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)

#pincode, country, state, phone no