from django.db import models
class users_input(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    search_period = models.DateTimeField(auto_now=True)
    
class new_loggers(models.Model):
    date_of_birth = models.DateField()
    Age = models.IntegerField()
    email = models.CharField(max_length=255)
    
    
