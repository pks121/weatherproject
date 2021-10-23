from django.db import models

# Create your models here.
class user(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	pwd = models.CharField(max_length = 50)
	class Meta:
		db_table = "user"
