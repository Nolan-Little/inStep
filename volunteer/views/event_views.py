import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization, Event, Shift, Volunteer, Venue
from volunteer.forms import EventForm, ShiftForm, VolSignUpForm


def new_event_template(request):
    org = Organization.objects.filter(user=request.user)[0]
    if request.method == "GET":
        new_event_form = EventForm()

        # create choice list based off of only that organizations related created venues
        venues = Venue.objects.filter(organization=org)
        new_event_form.fields['venue'].choices = [(venue.id, venue.name) for venue in venues]
        new_event_form.fields['venue'].choices.append(('','Add New Venue'))

        template_name = "events/new_event_template.html"
        return render(request, template_name, {"new_event_form": new_event_form})

    elif request.method == "POST":
        # TODO: organization cookies?
        form_data = request.POST

        selected_venue = form_data.get('venue', '')

        # create a new venue then create event
        if selected_venue == '':
            new_venue = Venue.objects.create(
                name=form_data['new_venue_name'],
                location=form_data['new_venue_location'],
                organization=org
            )

            event_form_data = {
                'name': form_data['name'],
                'description': form_data['description'],
            }

            new_event_form = EventForm(event_form_data)

            if new_event_form.is_valid():
                new_event = Event.objects.create(
                    name = event_form_data['name'],
                    description = event_form_data['description'],
                    venue = new_venue,
                    organization = org,
                    is_template = True
                )

                return HttpResponseRedirect(reverse('volunteer:dashboard'))

            else:
                template_name = "events/new_event_template.html"
                return render(request, template_name, {"new_event_form": new_event_form})

        # create event with selected venue
        else:
            event_form_data = {
                'name': form_data['name'],
                'description': form_data['description'],
                'venue': form_data['venue']
            }

            new_event_form = EventForm(event_form_data)

            if new_event_form.is_valid():
                new_event = Event.objects.create(
                    name = event_form_data['name'],
                    description = event_form_data['description'],
                    venue = Venue.objects.get(pk=int(event_form_data['venue'])),
                    organization = org,
                    is_template = True
                )
                return HttpResponseRedirect(reverse('volunteer:dashboard'))
            else:
                template_name = "events/new_event_template.html"
                return render(request, template_name, {"new_event_form": new_event_form})




def event_template_details(request, event_template_id):
    template_name = 'events/event_template_detail.html'
    context = {
        'event_template': Event.objects.get(pk=event_template_id)
    }
    return render(request, template_name, context)


def edit_event_template(request, event_template_id):
    if request.method == "GET":
        event_template = Event.objects.get(pk=event_template_id)
        template_name = "events/edit_event_template.html"

        event_form = EventForm(instance=event_template)

        context = {
            'edit_event_form': event_form,
            'event_template': event_template
        }

        return render(request, template_name, context)

    elif request.method == "POST":
        # TODO: org cookies?
        org = Organization.objects.filter(user=request.user)[0]
        form_data = request.POST

        selected_venue = form_data.get('venue', '')

        # create a new venue then create event
        if selected_venue == '':
            new_venue = Venue.objects.create(
                name=form_data['new_venue_name'],
                location=form_data['new_venue_location'],
                organization=org
            )

            event_form_data = {
                'name': form_data['name'],
                'description': form_data['description'],
            }

            new_event_form = EventForm(event_form_data)

            if new_event_form.is_valid():
                event_form_data['venue'] = new_venue
                Event.objects.filter(pk=event_template_id).update(**event_form_data)

                return HttpResponseRedirect(reverse('volunteer:dashboard'))

            else:
                template_name = "events/new_event_template.html"
                return render(request, template_name, {"new_event_form": new_event_form})

        # create event with selected venue
        else:
            event_form_data = {
                'name': form_data['name'],
                'description': form_data['description'],
                'venue': form_data['venue']
            }

            new_event_form = EventForm(event_form_data)

            if new_event_form.is_valid():
                Event.objects.filter(pk=event_template_id).update(**event_form_data)

                return HttpResponseRedirect(reverse('volunteer:dashboard'))
            else:
                template_name = "events/new_event_template.html"
                return render(request, template_name, {"new_event_form": new_event_form})

def schedule_event(request):
    # TODO: org cookies?
    org = Organization.objects.filter(user=request.user)[0]
    if request.method == "GET":
        template_name = "events/schedule_event.html"
        event_templates = org.event_set.filter(is_template=True)
        context = {
            "org": org,
            "event_templates": event_templates
        }

        return render(request, template_name, context)

    elif request.method == "POST":
        form_data = request.POST
        event_form_data = {
            'event': form_data['events'],
            'date': form_data['date'],
        }

        event = org.event_set.filter(pk=event_form_data['event'])[0]

        # Schedule Event
        scheduled_event = Event.objects.create(
            organization=org,
            name=event.name,
            description=event.description,
            venue=event.venue,
            location=event.location,
            date=event_form_data['date'],
            is_template=False
        )

        shift_templates = Shift.objects.filter(event_template=event)

        # # Schedule all appropriate shifts
        # for template in shift_templates:
        #     ScheduledShift.objects.create(
        #         scheduled_event=scheduled_event,
        #         shift_template=template
        #     )

    return HttpResponseRedirect(reverse('volunteer:dashboard'))


def sign_up(request, unique_url):
    if request.method == "GET":
        template_name = "events/sign_up.html"
        # scheduled_event = ScheduledEvent.objects.get(sign_up_url=unique_url)

        shift_list = list()
        # sched_shifts = ScheduledShift.objects.filter(
        #     scheduled_event=scheduled_event)
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
        # for shift in sign_up_form_data['shifts']:
        #     ShiftVolunteer.objects.create(
        #         notes=sign_up_form_data['notes'],
        #         volunteer=volunteer,
        #         scheduled_shift=ScheduledShift.objects.get(pk=shift)
        #     )

        return HttpResponseRedirect(reverse('volunteer:dashboard'))
