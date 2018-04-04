from django.conf.urls import url
from django.conf import settings
from django.views import static
from django.views.static import serve
from . import views

urlpatterns = [
   url(r'^$', views.home, name = 'home'),
   url(r'^user/(\w+)/$', views.profile, name='profile'),
   url(r'^([0-9]+)/$',views.detail,name = 'detail'),
   url(r'^login/$', views.login, name='login'),
   url(r'^logout/$', views.logout, name='logout'),
   url(r'^registration/$', views.registration, name='registration'),
   url(r'^search/$' , views.search),
   url(r'^places/$' , views.places, name= 'places'),
   url(r'^contact/$', views.contact, name='contact'),
   url(r'^feedback/$', views.feedback, name='feedback'),
   url(r'^thanks/$', views.thanks, name='thanks'),
]




 
if settings.DEBUG:
	urlpatterns += [
		url(r'^media/(?P<path>.*)$', serve,
		   {'document_root': settings.MEDIA_ROOT,}),
	]