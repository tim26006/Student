from django.db import models

# Create your models here.


class Sub(models.Model):
  name = models.CharField(max_length=50)
  group = models.CharField(max_length=10)




