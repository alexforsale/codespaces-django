from django.db import models

# Create your models here.
class CloudHost(models.Model):
    cookie_id = models.CharField(max_length=56)
    id = models.IntegerField()
    name = models.EmailField()
    first_name = models.CharField(max_length=30)