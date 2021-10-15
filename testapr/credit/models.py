from django.db import models

# Create your models here.

class CreditModel(models.Model):
    title = models.CharField(max_length=100)
    user = models.CharField(max_length=50)
    creditstatus = models.CharField(max_length=50)
    others = models.TextField()
