from django.db import models

# Create your models here.

class User(models.Model):
	name=models.CharField(max_length=1500)
 	img = models.ImageField(upload_to='media/users/')
 	def __unicode__(self):
 		return self.name





class Service(models.Model):
	service_name=models.CharField(max_length=1500)
	service_desc=models.CharField(max_length=1500)
	service_url=models.URLField(null=True, blank=True)
	def __unicode__(self):
		return self.service_name


class Client(models.Model):
	client_name=models.CharField(max_length=1500)
	client_address=models.CharField(max_length=1500)
	client_desc=models.CharField(max_length=1500)
	def __unicode__(self):
		return self.client_name



class New(models.Model):
	new_title=models.CharField(max_length=1500)
	new_desc=models.CharField(max_length=1500)
	new_date=models.DateField()
	new_img=models.ImageField(upload_to='media/news/')
	def __unicode__(self):
		return self.new_title


class Product(models.Model):
	product_name=models.CharField(max_length=1500)
	product_desc=models.CharField(max_length=1500)
	product_img=models.ImageField(upload_to='media/products/')
	def __unicode__(self):
		return self.product_name


class Menu(models.Model):
	menu_title=models.CharField(max_length=1500)
	menu_link=models.CharField(max_length=1500)
	def __unicode__(self):
		return self.menu_title



class Slider(models.Model):
	#img_captha=models.CharField(max_length=1500)
	img_path=models.ImageField(upload_to='media/imgs/')

		


		