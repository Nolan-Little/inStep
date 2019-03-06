from django.contrib.auth.models import User
from django import forms
from volunteer.models import Organization, EventTemplate, ScheduledEvent, ShiftTemplate


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


class ShiftTemplateForm(forms.ModelForm):

    class Meta:
        model = ShiftTemplate
        fields = ('start_time', 'end_time', 'num_volunteers', 'description')

        widgets = {
            'start_time': forms.TimeInput(attrs={"type": "time"}),
            'end_time': forms.TimeInput(attrs={"type": "time"}),
            'description': forms.Textarea(attrs={"type": "textArea"})
        }


class VolSignUpForm(forms.Form):
    def __init__(self, **kwargs):
        shift_choices = kwargs.pop('shift_choices')
        super(VolSignUpForm, self).__init__(**kwargs)

        self.fields['shifts'] = forms.MultipleChoiceField(
            label='Select Shifts',
            widget=forms.CheckboxSelectMultiple,
            choices=(shift_choices)
        )

    name = forms.CharField(max_length=75, required=True)
    notes = forms.CharField(max_length=150, required=True)


