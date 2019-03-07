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
    url(r'^event_template_details/(?P<event_template_id>\d+)/$', views.event_template_details, name="event_template_details"),
    url(r'^edit_event_template/(?P<event_template_id>\d+)/$', views.edit_event_template, name="edit_event_template"),
    url(r'^new_shift_template/(?P<event_template_id>\d+)/$', views.new_shift_template, name="new_shift_template"),
    url(r'^edit_shift/(?P<shift_id>\d+)/$', views.edit_shift, name="edit_shift"),
    url(r'^schedule_event', views.schedule_event, name="schedule_event"),
    url(r'^sign_up/(?P<unique_url>[-\w]+)', views.sign_up, name="sign_up"),
]