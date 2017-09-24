from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^login$', views.login),
    #url(r'^list$', views.devi, name='devi'),
    url(r'^client$', views.add, name='add_client'),
]
