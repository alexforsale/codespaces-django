from django.db import models

# Create your models here.
class CloudHost(models.Model):
    cookie_id = models.CharField(max_length=56)
    id = models.IntegerField()
    name = models.EmailField()
    first_name = models.CharField(max_length=30)
    avatar = models.URLField()
    email = models.EmailField()
    personal_id_number = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField()
    user_id = models.IntegerField()
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    updated_at = models.DateTimeField()
    signup_site = models.CharField(max_length=30)
