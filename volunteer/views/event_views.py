import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization, EventTemplate, ScheduledEvent, ShiftTemplate, ScheduledShift, Volunteer, ShiftVolunteer
from volunteer.forms import EventTemplateForm, ShiftTemplateForm, VolSignUpForm

NUM_SHIFT_INPUT_GROUP_VALS = 4


def new_event_template(request):
    if request.method == "GET":
        new_event_form = EventTemplateForm()
        template_name = "events/new_event_template.html"
        return render(request, template_name, {"new_event_form": new_event_form})

    elif request.method == "POST":
        form_data = request.POST

        event_form_data = {
            'name': form_data['name'],
            'description': form_data['description'],
            'venue': form_data['venue'],
            'location': form_data['location']
        }

        new_org_form = EventTemplateForm(event_form_data)
        if new_org_form.is_valid():
            org = Organization.objects.filter(user=request.user)[0]
            new_event_template = EventTemplate.objects.create(
                name=event_form_data['name'],
                description=event_form_data['description'],
                venue=event_form_data['venue'],
                location=event_form_data['location'],
                organization=org
            )

            return HttpResponseRedirect(reverse('volunteer:new_shift_template', args=(new_event_template.id, )))

        else:
            template_name = 'events/new_event_template.html'
            return render(request, template_name, {'new_event_form': new_event_form})


def event_template_details(request, event_template_id):
    template_name = 'events/event_template_detail.html'
    context = {
        'event_template': EventTemplate.objects.get(pk=event_template_id)
    }
    return render(request, template_name, context)


def edit_event_template(request, event_template_id):
    if request.method == "GET":
        event_template = EventTemplate.objects.get(pk=event_template_id)
        template_name = "events/edit_event_template.html"
        event_form_data = {
                'name': event_template.name,
                'description': event_template.description,
                'venue': event_template.venue,
                'location': event_template.location
            }

        context = {
        'edit_event_form':EventTemplateForm(event_form_data),
        'event_template': event_template
        }

        return render(request, template_name, context)

    if request.method == "POST":
        form_data = request.POST
        event_form_data = {
            'name': form_data['name'],
            'description': form_data['description'],
            'venue': form_data['venue'],
            'location': form_data['location']
        }

        new_org_form = EventTemplateForm(event_form_data)

        if new_org_form.is_valid():
            event_template = EventTemplate.objects.filter(pk=event_template_id).update(**event_form_data)

            return HttpResponseRedirect(reverse('volunteer:dashboard'))



def schedule_event(request):
    org = Organization.objects.filter(user=request.user)[0]
    if request.method == "GET":
        template_name = "events/schedule_event.html"

        context = {
            "org": org
        }

        return render(request, template_name, context)

    elif request.method == "POST":
        form_data = request.POST
        event_form_data = {
            'event': form_data['events'],
            'date': form_data['date'],
        }

        event = org.eventtemplate_set.filter(pk=event_form_data['event'])[0]

        # Schedule Event
        scheduled_event = ScheduledEvent.objects.create(
            date=event_form_data['date'],
            event_template=event
        )

        shift_templates = ShiftTemplate.objects.filter(event_template=event)

        # Schedule all appropriate shifts
        for template in shift_templates:
            ScheduledShift.objects.create(
                scheduled_event=scheduled_event,
                shift_template=template
            )

    return HttpResponseRedirect(reverse('volunteer:dashboard'))


def sign_up(request, unique_url):
    if request.method == "GET":
        template_name = "events/sign_up.html"
        scheduled_event = ScheduledEvent.objects.get(sign_up_url=unique_url)

        shift_list = list()
        sched_shifts = ScheduledShift.objects.filter(
            scheduled_event=scheduled_event)
        for shift in sched_shifts:
            shift_list.append(
                (shift.id, f'{shift.shift_template.start_time.strftime("%-I:%M%p")} - {shift.shift_template.end_time.strftime("%-I:%M%p")} {shift.shift_template.description}'))
        shift_choices = tuple(shift_list)
        shift_form = VolSignUpForm(shift_choices=shift_choices)

        context = {
            'scheduled_event': scheduled_event,
            'shift_form': shift_form,
            'unique_url': unique_url
        }

        return render(request, template_name, context)

    if request.method == "POST":
        form_data = request.POST
        print(form_data)
        sign_up_form_data = {
            'name': form_data['name'],
            'notes': form_data['notes'],
            'shifts': form_data.getlist('shifts')
        }

        volunteer = Volunteer.objects.create(name=sign_up_form_data['name'])
        print(sign_up_form_data['shifts'])
        for shift in sign_up_form_data['shifts']:
            ShiftVolunteer.objects.create(
                notes=sign_up_form_data['notes'],
                volunteer=volunteer,
                scheduled_shift=ScheduledShift.objects.get(pk=shift)
            )

        return HttpResponseRedirect(reverse('volunteer:dashboard'))
