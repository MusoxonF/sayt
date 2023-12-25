from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .models import User
from .forms import UserForm, LoginForm
from news.models import Like, News


def signup(request):
	form = UserForm()
	if request.method == 'POST':
		form = UserForm(data=request.POST, files = request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'signup.html', {'form':form})
	return render(request, 'signup.html', {'form':form})


def Login(request):
	login_form = LoginForm()
	if request.method == 'POST':
		login_form = LoginForm(data=request.POST)
		if login_form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
		return render(request, 'login.html', {'login_form':login_form})

	return render(request, 'login.html', {'login_form':login_form})


def Logout(request):
	logout(request)
	return redirect('home')


def Profile(request):
	profile = UserForm(instance=request.user)
	return render(request, 'profile.html', {'profile':profile})


def like(request, id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			news = News.objects.get(id=id)
			if Like.objects.filter(news=news):
				l = Like.objects.filter(news=news).first()
				if request.user in l.user.all():
					l.user.remove(request.user)
					return redirect('home')
				l.user.add(request.user)
				return redirect('home')
	
			like = Like.objects.create(
				news=news
				)
			like.user.add(request.user)
			return redirect('home')