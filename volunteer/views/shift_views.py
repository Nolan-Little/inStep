import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization, Event, Shift, Volunteer
from volunteer.forms import EventForm, ShiftForm, VolSignUpForm

def new_shift(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == "GET":
        current_shifts = Shift.objects.filter(event=event)
        template_name = 'events/shift_template.html'
        shift_form = ShiftForm()
        context = {
            'event': event,
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

        Shift.objects.create(
            start_time=event_form_data['start_time'],
            end_time=event_form_data['end_time'],
            num_volunteers=event_form_data['num_volunteers'],
            description=event_form_data['description'],
            event=event
        )

        if form_data.get('add_shift'):
            return HttpResponseRedirect(reverse('volunteer:new_shift', args=(event.id, )))

        elif form_data.get('dashboard'):
            return HttpResponseRedirect(reverse('volunteer:event_template_details', args=(event.id,)))

def edit_shift(request, shift_id):
    if request.method == "GET":
        template_name = "events/edit_shift.html"
        shift =  Shift.objects.get(pk=shift_id)

        shift_form_data = {
                'start_time': shift.start_time,
                'end_time': shift.end_time,
                'num_volunteers': shift.num_volunteers,
                'description': shift.description
            }

        shift_form = ShiftForm(shift_form_data)
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

        shift_form = ShiftForm(shift_form_data)

        if shift_form.is_valid():
            shift = Shift.objects.get(pk=shift_id)
            Shift.objects.filter(pk=shift_id).update(**shift_form_data)

            return HttpResponseRedirect(reverse('volunteer:event_template_details', args=(shift.event.id,)))


def delete_shift(request, shift_id):
    redirect_url = request.META['HTTP_REFERER']
    shift = Shift.objects.get(id=shift_id)
    shift.delete()
    return HttpResponseRedirect(redirect_url)


def sign_up(request, unique_url):
    if request.method == "GET":
        template_name = "events/sign_up.html"
        scheduled_event = Event.objects.get(sign_up_url=unique_url)

        shift_list = list()
        sched_shifts = Shift.objects.filter(event=scheduled_event)
        for shift in sched_shifts:
            if shift.slots_remaining > 0:
                shift_list.append(
                    (shift.id, f'{shift.start_time.strftime("%-I:%M%p")} - {shift.end_time.strftime("%-I:%M%p")} {shift.description}'))
        shift_choices = tuple(shift_list)
        shift_form = VolSignUpForm(shift_choices=shift_choices)

        context = {
            'scheduled_event': scheduled_event,
            'shift_form': shift_form,
            'unique_url': unique_url
        }

        return render(request, template_name, context)

    if request.method == "POST":
        template_name = "events/confirm.html"
        form_data = request.POST

        sign_up_form_data = {
            'name': form_data['name'],
            'notes': form_data['notes'],
            'shifts': form_data.getlist('shifts')
        }

        shift_list = list()
        for shift in sign_up_form_data['shifts']:
            shift_list.append(Shift.objects.get(pk=shift))
            Volunteer.objects.create(
                name=sign_up_form_data['name'],
                note=sign_up_form_data['notes'],
                shift=Shift.objects.get(pk=shift)
            )

        organizer_email = shift_list[0].event.organization.user.all()[0].email

        context = {
            "name": form_data['name'],
            'shifts': shift_list,
            'organizer_email': organizer_email
        }

        return render(request, template_name, context)