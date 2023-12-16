from django.shortcuts import render, redirect
from .forms import NewsForm, CommentForm

from .models import News
from user.models import User
from django.views import View
from .models import Comment as CommentModel


class Create_news(View):
	def get(self, request):
		form = NewsForm()
		return render(request, 'create.html', {'form': form})

		
	def post(self, request):
		form = NewsForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'create.html', {'form':form})
	
class Edit(View):
	def get(self, request):
		news = News.objects.get(id=id)
		form = NewsForm(instance=news)
		return render(request, 'create.html', {'form': form})
	def post(self, request):
		form = NewsForm(instance=news, data = request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		return render(request, 'create.html', {'form': form} )
	
class Comment(View):
	def post(self, request):
		if form.is_valid():
			form.save()
			return redirect('detail', id)

def delete(request, id):
	news = News.objects.get(id=id)
	news.delete()
	return redirect('home')


def delete_comment(request, id):
	comment = CommentModel.objects.get(id=id)
	comment.delete()
	return redirect('home')


def detail(request, id):
	news=News.objects.get(id=id)
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(data=request.POST)
		if form.is_valid():
			comment = form.cleaned_data['comment']
			CommentModel.objects.create(
					comment = comment,
					news = news,
					author = request.user,
					)
			return redirect('home')
	return render(request, 'detail.html', {'news':news, 'form':form})

