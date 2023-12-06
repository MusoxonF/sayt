from django.urls import path
from .views import signup, Login, Logout, Profile, like 


urlpatterns = [
	path('signup', signup, name = 'signup'),
	path('Login', Login, name = 'Login'),
	path('Logout', Logout, name = 'Logout'),
	path('Profile/', Profile, name = 'Profile'),
	path('like/<int:id>', like, name='like'),

]	