from django.conf.urls import *
from update import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns(
    '',
    url( r'^update/$' , login_required( views.update ) , name = "update" ),
    url( r'^linktwitter/$' , login_required( views.link_twitter ) , name = "linktwitter" ),
    url( r'^oatwitter/$' , login_required( views.oa_twitter ) , name = "oatwitter" ),
)