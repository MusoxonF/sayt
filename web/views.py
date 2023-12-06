from django.shortcuts import render 
from django.core.paginator import Paginator
from news.models import News

def home(request):
	news = News.objects.all()
	page = Paginator(news, 4)
	number = request.GET.get('page', 1)
	pages = page.page(number)
	find = request.GET.get('find', None)
	if find:
		new = News.objects.filter(title__icontains=find)
		return render(request, 'home.html', {'new':new } )
	return render(request, 'home.html', {'news':pages} )
