from django.db import models

# Create your models here.
class Restaurant(models.Model):
	Name = models.CharField(max_length=120)
	Description = models.TextField()
	Opening_time = models.TimeField
	Closing_time = models.TimeField
	"""docstring for ClassName"""
