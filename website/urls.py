from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register', views.registration, name= 'register'),
    url(r'^verify', views.verification, name= 'verify'),
    url(r'^event', views.event, name='event'),
    url(r'^demo', views.demo, name='demo'),
    url(r'^showevents', views.showevents, name='showevents')
]