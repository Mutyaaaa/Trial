from django.db import models
from student.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Consumables(models.Model):
	availability= (
		('Available', 'Available'),
		('Unavailable', 'Unavailable'),
	)
	name_of_consumables = models.CharField(max_length = 100)
	avail = models.CharField(max_length = 15, choices= availability, blank = True)
	consumables_picture = models.CharField(max_length = 1000)

	def __str__(self): #specify what to print out
		return self.name_of_consumables

class Cart2(models.Model):
	availability= (
		('Available', 'Available'),
		('Unavailable', 'Unavailable'),
	)
	user_c = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	name_of_consum = models.CharField(max_length = 100)	
	avail = models.CharField(max_length = 15, choices= availability, blank = True)
	consum_picture = models.CharField(max_length = 1000, null=True)

	def __str__(self): #specify what to print out
		return self.name_of_consum
	