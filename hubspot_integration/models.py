from django.db import models

# Create your models here.


class Deal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='active')  # Example field
