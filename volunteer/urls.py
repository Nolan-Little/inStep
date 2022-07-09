from django.urls import re_path

from . import views

app_name = "volunteer"

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'login$', views.login_user, name='login'),
    re_path(r'logout$', views.user_logout, name='logout'),
    re_path(r'register$', views.register, name='register'),
    re_path(r'new_org', views.new_org, name="new_org"),
    re_path(r'profile', views.profile, name="profile"),
    re_path(r'edit_profile', views.edit_profile, name="edit_profile"),
    re_path(r'dashboard', views.dashboard, name="dashboard"),
    re_path(r'new_event_template', views.new_event_template, name="new_event_template"),
    re_path(r'event_template_details/(?P<event_template_id>\d+)/$', views.event_template_details, name="event_template_details"),
    re_path(r'edit_event_template/(?P<event_template_id>\d+)/$', views.edit_event_template, name="edit_event_template"),
    re_path(r'delete_event/(?P<event_id>\d+)/$', views.delete_event, name="delete_event"),
    re_path(r'delete_event_confirm/(?P<event_id>\d+)/$', views.delete_event_confirm, name="delete_event_confirm"),
    re_path(r'new_shift_template/(?P<event_id>\d+)/$', views.new_shift, name="new_shift"),
    re_path(r'edit_shift/(?P<shift_id>\d+)/$', views.edit_shift, name="edit_shift"),
    re_path(r'delete_shift/(?P<shift_id>\d+)/$', views.delete_shift, name="delete_shift"),
    re_path(r'delete_volunteer/(?P<volunteer_id>\d+)/$', views.delete_volunteer, name="delete_volunteer"),
    re_path(r'schedule_event/(?P<event_template_id>\d+)/$', views.schedule_event, name="schedule_event"),
    re_path(r'sign_up/(?P<unique_url>[-\w]+)', views.sign_up, name="sign_up"),
]