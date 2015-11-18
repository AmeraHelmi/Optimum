from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import *

def start(request):
	users=User.objects.all()
	menu_items=Menu.objects.all()
	services=Service.objects.all()
	clients=Client.objects.all()
	news=New.objects.all()
	products=Product.objects.all()
	slider_images=Slider.objects.all()
	return render(request,'home-01.html',{'users':users,'services':services,'products':products,'menu_items':menu_items,'news':news,'clients':clients,'slider_images':slider_images})




def gallery(request):
	users=User.objects.all()
	return render(request,'test.html',{'users':users})

def services(request):
	users=User.objects.all()
	menu_items=Menu.objects.all()
	services=Service.objects.all()
	clients=Client.objects.all()
	news=New.objects.all()
	products=Product.objects.all()
	slider_images=Slider.objects.all()
	return render(request,'services.html',{'users':users,'services':services,'products':products,'menu_items':menu_items,'news':news,'clients':clients,'slider_images':slider_images})

def clients(request):
	users=User.objects.all()
	menu_items=Menu.objects.all()
	services=Service.objects.all()
	clients=Client.objects.all()
	news=New.objects.all()
	products=Product.objects.all()
	slider_images=Slider.objects.all()
	return render(request,'clients.html',{'users':users,'services':services,'products':products,'menu_items':menu_items,'news':news,'clients':clients,'slider_images':slider_images})

def products(request):
	users=User.objects.all()
	menu_items=Menu.objects.all()
	services=Service.objects.all()
	clients=Client.objects.all()
	news=New.objects.all()
	products=Product.objects.all()
	slider_images=Slider.objects.all()
	return render(request,'products.html',{'users':users,'services':services,'products':products,'menu_items':menu_items,'news':news,'clients':clients,'slider_images':slider_images})

