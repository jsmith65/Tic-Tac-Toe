from django.conf.urls import patterns, url

from XandO import views

urlpatterns = patterns('',
	url(r'^$', views.playGame, name='Play Tic-Tac-Toe')
	)