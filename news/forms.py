from django import forms
from .models import News, Comment

class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = ['title', 'content', 'category', 'photo']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']