from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

	STATUS = (
	('admin', 'ADMIN'),
	('manager', 'MANAGER'),
	('user', 'USER'),
	)


	address = models.CharField(max_length= 30, null=True)
	phone = models.CharField(max_length=13)
	image = models.ImageField(upload_to = 'user_photos/', null = True, blank = True)
	status = models.CharField(max_length = 10, choices=STATUS, default = "user")
	def __str__(self):
		return self.username
