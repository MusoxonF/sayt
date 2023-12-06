from django.contrib import admin
from .models import Category, News, Comment

class NewsAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

	class Meta:
		model = News

admin.site.register(Category)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment)

