from django.conf.urls import patterns, include, url

from django.contrib import admin
from main import views
from karatekyokushin import views2
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^karatekyokushin/', views2.KarateKyokushinMain, name='KarateKyokushinMain'),
    url(r'^create/', views2.KarateKyokushinCreate, name='KarateKyokushinCreate'),
    url(r'^signUp/', views.signUp, name='signUp'),
    url(r'^signIn/', views.signIn, name='signIn'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^tournament/(?P<tournament_id>\d+)/', views2.tournament, name='tournament'),
)
