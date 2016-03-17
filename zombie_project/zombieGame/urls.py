from django.conf.urls import patterns, url
from zombieGame import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.login, name='login'),
        url(r'^profile/$', views.profile, name='profile'),
        url(r'^game/$', views.game, name='game'),
        url(r'^leaderboard/$', views.leaderboard, name='leaderboard')
        )