import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization, EventTemplate, ScheduledEvent, ShiftTemplate, ScheduledShift, Volunteer, ShiftVolunteer
from volunteer.forms import EventTemplateForm, ShiftTemplateForm, VolSignUpForm

def new_shift_template(request, event_template_id):
    event_template = EventTemplate.objects.get(pk=event_template_id)

    if request.method == "GET":
        current_shifts = ShiftTemplate.objects.filter(
            event_template=event_template)
        template_name = 'events/shift_template.html'
        shift_form = ShiftTemplateForm()
        context = {
            'event_template': event_template,
            'shift_form': shift_form,
            'current_shifts': current_shifts
        }
        return render(request, template_name, context)

    elif request.method == "POST":
        form_data = request.POST
        event_form_data = {
            'start_time': form_data['start_time'],
            'end_time': form_data['end_time'],
            'description': form_data['description'],
            'num_volunteers': form_data['num_volunteers']
        }

        new_shift_template = ShiftTemplate.objects.create(
            start_time=event_form_data['start_time'],
            end_time=event_form_data['end_time'],
            num_volunteers=event_form_data['num_volunteers'],
            description=event_form_data['description'],
            event_template=event_template
        )

        return HttpResponseRedirect(reverse('volunteer:new_shift_template', args=(event_template.id, )))

def edit_shift(request, shift_id):
    if request.method == "GET":
        template_name = "events/edit_shift.html"
        shift =  ShiftTemplate.objects.get(pk=shift_id)

        shift_form_data = {
                'start_time': shift.start_time,
                'end_time': shift.end_time,
                'num_volunteers': shift.num_volunteers,
                'description': shift.description
            }

        shift_form = ShiftTemplateForm(shift_form_data)
        context = {
            'shift_form': shift_form,
            'shift': shift
        }

        return render(request, template_name, context)

    if request.method == "POST":
        form_data = request.POST

        shift_form_data = {
            'start_time': form_data['start_time'],
            'end_time': form_data['end_time'],
            'num_volunteers': form_data['num_volunteers'],
            'description': form_data['description']
        }

        shift_form = ShiftTemplateForm(shift_form_data)

        if shift_form.is_valid():
            shift = ShiftTemplate.objects.get(pk=shift_id)
            ShiftTemplate.objects.filter(pk=shift_id).update(**shift_form_data)

            return HttpResponseRedirect(reverse('volunteer:event_template_details', args=(shift.event_template.id,) ))


