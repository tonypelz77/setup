from django.conf.urls import patterns, url
from options import views

urlpatterns = patterns(' ',
	url(r'^$', views.index, name = 'index'),
	url(r'^index', views.index, name = 'index'),
	url(r'^about/', views.about, name = 'about'),
	url(r'^contact/', views.contact, name = 'contact'),
	url(r'^otkf/', views.otkf, name = 'otkf'),
	url(r'^bth/', views.bth, name = 'bth'),
	url(r'^chimera/', views.chimera, name = 'chimera'),
	url(r'^email/', views.email, name = 'email'),
	)