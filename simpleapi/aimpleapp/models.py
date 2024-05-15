from django.db import models

# Create your models here.

class SampleUser(models.Model):
    name = models.CharField(max_length = 255, db_index = True, default = '', null = False)
    email = models.EmailField(max_length = 255, unique = True, null = False)
    age = models.IntegerField(max_length = 255, null = False)
    account = models.DecimalField(decimal_places = 2, max_digits = 255)
