from django.contrib.auth.models import User
from django import forms
from volunteer.models import Organization, EventTemplate, ScheduledEvent


class UserForm(forms.ModelForm):
    # Form class to create a new user
    # Author: Brad Davis
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)


class OrgForm(forms.ModelForm):

    class Meta:
        model = Organization
        fields = ('name', 'description')


class EventTemplateForm(forms.ModelForm):

    class Meta:
        model = EventTemplate
        fields = ('name', 'description', 'venue', 'location')
