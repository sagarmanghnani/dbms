from django.conf.urls import url
from website import views

app_name =  'website'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register/$', views.registration, name= 'register'),
    url(r'^verify/$', views.verification, name= 'verify'),
    url(r'^event/$', views.event, name='event'),
    url(r'^demo/$', views.demo, name='demo'),
    url(r'^showevents/$', views.showevents, name='showevents'),
    url(r'^trial/$', views.trial, name='trial'),
    url(r'^edit/$', views.edit_form, name='edit_form'),
    url(r'^another/$', views.another, name='another'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^city/$', views.city_val, name='city'),
    url(r'^hello/$', views.city_events, name='cityevent'),
    url(r'^details_event/(?P<city_id>[0-9]+)', views.details_event, name='details_event'),
    url(r'^eventreg', views.show_reg_events, name='eventregistration'),
    url(r'^registerevent/(?P<event_id>[0-9]+)', views.registerevent, name='registerevent'),
    url(r'^userevent/$', views.user_event, name='userevent'),
    url(r'^leavemeetup/(?P<leave_id>[0-9]+)', views.leavemeetup, name='leavemeetup'),
    url(r'^upcoming', views.upcomingevent, name='upcomingevent'),
    url(r'^getquest', views.get_quest, name='getquest'),
    url(r'selchoice', views.sel_choice, name='sel_choice'),
    url(r'^getuser', views.getting_user, name='getuser'),
    url(r'^verifyuser', views.verifyuser, name='verifyuser'),
    url(r'^newpassword', views.newpassword, name='newpassword'),
    url(r'^redirecting', views.redirecting, name='redirecting'),
    url(r'^showdel/(?P<del_id>[0-9]+)', views.showdel, name='showdel'),
    url(r'^edit_form/(?P<edit_id>[0-9]+)', views.edit_form, name='edit_form'),


]