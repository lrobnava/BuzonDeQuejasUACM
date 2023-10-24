from django.db import models

class Quejas(models.Model):
    idQueja = models.AutoField(primary_key=True)
    user = models.CharField(max_length=255)
    type = models.CharField(max_length=30)
    quejaText = models.CharField(max_length=500)
