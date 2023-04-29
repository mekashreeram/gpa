from django.db import models

# Create your models here.

class Marks(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length = 20, default="newsub")
  credit = models.FloatField(default=3)
  grade = models.IntegerField(default=10)
  factor = models.CharField(max_length=30, default="mekashreeram")