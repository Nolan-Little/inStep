from django.conf.urls import url

from . import views

app_name = "volunteer"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^new_org', views.new_org, name="new_org")
]