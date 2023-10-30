from django.db import models

# Create your models here.


class Student(models.Model):

  name = models.CharField(max_length=50)
  group = models.CharField(max_length=10)


class Todo(models.Model):
  sub = models.CharField(max_length=20)
  task = models.CharField(max_length=100)

