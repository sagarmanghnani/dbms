from django.conf.urls import url
from website import views

app_name =  'website'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register', views.registration, name= 'register'),
    url(r'^verify', views.verification, name= 'verify'),
    url(r'^event', views.event, name='event'),
    url(r'^demo', views.demo, name='demo'),
    url(r'^showevents', views.showevents, name='showevents'),
    url(r'^trial', views.trial, name='trial'),
    url(r'^edit', views.edit_form, name='edit_form'),
    url(r'^another', views.another, name='another'),
    url(r'^delete', views.delete, name='delete'),
    url(r'^city', views.city_val, name='city'),
    url(r'^hello', views.city_events, name='cityevent'),
    url(r'^details_event/(?P<city_id>[0-9]+)', views.details_event, name='details_event'),
    url(r'^playing', views.playing, name='playing'),

]