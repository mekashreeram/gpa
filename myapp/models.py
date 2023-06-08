from django.db import models

class Marks(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length = 20, default="newsub")
  credit = models.FloatField(default=3)
  grade = models.IntegerField(default=10)
  factor = models.CharField(max_length=30, default="mekashreeram")

class Profile(models.Model):
  factor = models.CharField(max_length=30, primary_key=True)
  targetgpa = models.FloatField(default=0)
  nosc = models.FloatField(default=0)
  Sem1 = models.FloatField(default=0)
  Sem2 = models.FloatField(default=0)
  Sem3 = models.FloatField(default=0)
  Sem4 = models.FloatField(default=0)
  Sem5 = models.FloatField(default=0)
  Sem6 = models.FloatField(default=0)
  Sem7 = models.FloatField(default=0)
  Sem8 = models.FloatField(default=0)