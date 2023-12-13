from django.urls import path
from .views import Create_news, Edit, delete, detail

urlpatterns = [
	path('Create_news/', Create_news.as_view(), name='create'),
	path('edit/<int:id>', Edit.as_view(), name='edit'),
	path('delete/<int:id>', delete, name='delete'),
	path('detail/<int:id>', detail, name="detail"),


]