from django.conf.urls import url
from . import views

app_name='polls'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<doloto_id>[0-9]+)/ybt/$', views.selectYbt, name='ybt'),
	url(r'^calculate/$', views.loadCalc, name='calc'),
	url(r'change', views.changeDoloto, name='change'),
	url(r'selectYbt', views.changeYBT, name='selYbt'),
	url(r'selectCasing', views.changeCasing, name='selCas'),
	url(r'^getAnswer/$', views.getAnswer, name='getAnswer'),
	url(r'^history/$', views.historyLoad, name='histor'),
	url(r'^auth/$', views.authUser, name='auth'),
	url(r'^logout/$', views.logoutBtn, name='logoutBtn'),
	url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
	url(r'^help/$', views.help, name='help'),
	url(r'^delete/$', views.clearHistory, name='delete'),

]