from django.db import models
from django.contrib.auth.models import User

class Todos(models.Model):
	title = models.CharField(max_length = 100, blank = False)
	memo = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'images/', null = True)
	createdon = models.DateTimeField(auto_now_add = True)
	datecompleted = models.DateTimeField(null = True, blank = True)
	important = models.BooleanField(default = False)
	user = models.ForeignKey(User, on_delete = models.CASCADE)


	def __str__(self):
		return self.title
