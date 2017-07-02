from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home,name='index'),
    url(r'^profile/$', views.update_profile),
    url(r'^account/logout/$', views.Logout),
    url(r'^map/add/$', views.model_form_upload, name='create_map'),
]
