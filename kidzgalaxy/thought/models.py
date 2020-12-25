from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Thought(models.Model):
    thought_id = models.IntegerField()
    thought_date = models.CharField(max_length=30)
    thought = models.CharField(max_length=250)
