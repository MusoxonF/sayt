from django.db import models
from user.models import User
from django.utils.text import slugify


class Category(models.Model):
	name = models.CharField(max_length = 50)

	def __str__(self):
		return self.name


class News(models.Model):
	title = models.CharField(max_length = 150, verbose_name = 'Xabar sarlavhasi')
	content = models.TextField(verbose_name = 'Xabar matni')
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'User_news')
	photo = models.ImageField(upload_to = 'news_photo/', null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank = True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)


	def __str__(self):
		return self.title

	@property
	def sum_of_likes(self):
		return self.likes.user.count() 

	@property
	def sum_of_dislikes(self):
		return self.dislikes.user.count()


class Comment(models.Model):
	comment = models.TextField(verbose_name = 'Izoh')
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	news = models.ForeignKey(News, on_delete = models.CASCADE, related_name='news_comments')

	def __str__(self):
		return self.comment


class Like(models.Model):
	news = models.OneToOneField(News, on_delete=models.CASCADE, related_name = 'likes')
	user = models.ManyToManyField(User)


class Dislike(models.Model):
	news = models.OneToOneField(News, on_delete=models.CASCADE, related_name = 'dislikes')
	user = models.ManyToManyField(User)
