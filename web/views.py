from django.shortcuts import render 
from django.core.paginator import Paginator
from news.models import News

from rest_framework.views import APIView
from rest_framework.response import Response


class RestView(APIView):
	def get(self, requests):
		f = News.objects.all()
		d = {}
		l = []
		for i in f:
			data = {}
			data['title'] = i.title
			data['content'] = i.content
			l.append(data)
		d['all_news'] = l
		return Response(d)

	def post(self, requests):
		print(request.data)

		return Response({"message": 'yaratildi'})

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
