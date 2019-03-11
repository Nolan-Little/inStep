from django.contrib.auth.models import User
from django import forms
from volunteer.models import Organization, Event, Shift, Shift


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


class EventForm(forms.ModelForm):
    new_venue_name = forms.CharField(max_length=75, required=False)
    new_venue_location = forms.CharField(max_length=150, required=False)

    class Meta:
        model = Event
        fields = ('name', 'description', 'venue', 'new_venue_name', 'new_venue_location')

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['venue'].empty_label = "Add New Venue"
        # following line needed to refresh widget copy of choice list
        self.fields['venue'].widget.choices = self.fields['venue'].choices


class ShiftForm(forms.ModelForm):

    class Meta:
        model = Shift
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


