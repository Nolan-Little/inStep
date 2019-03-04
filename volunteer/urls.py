from django.conf.urls import url

from . import views

app_name = "volunteer"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^new_org', views.new_org, name="new_org"),
    url(r'^dashboard', views.dashboard, name="dashboard"),
    url(r'^new_event_template', views.new_event_template, name="new_event_template"),
    url(r'^schedule_event', views.schedule_event, name="schedule_event"),
    url(r'^sign_up/(?P<unique_url>[-\w]+)', views.sign_up, name="sign_up"),
]