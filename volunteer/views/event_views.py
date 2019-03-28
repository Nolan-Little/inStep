import datetime
import calendar
from collections import OrderedDict
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization, Event, Shift, Volunteer, Venue
from volunteer.forms import EventForm, ShiftForm, VolSignUpForm
from volunteer.modules.calenders import month_cal

@login_required
def new_event_template(request):
    '''View to handle creating an event blueprint

    Arguments:
        request {object} -- http request object
        event_template_id {int} -- event object id

    Returns:
        render -- If request method is GET then it renders the form
        if the request is a POST then it performs the proper create and renders the dashboard.
    '''
    # TODO: organization cookies?
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

                return HttpResponseRedirect(reverse('volunteer:new_shift', args=(new_event.id,)))

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
                return HttpResponseRedirect(reverse('volunteer:new_shift', args=(new_event.id,)))
            else:
                template_name = "events/new_event_template.html"
                return render(request, template_name, {"new_event_form": new_event_form})



@login_required
def event_template_details(request, event_template_id):
    template_name = 'events/event_template_detail.html'
    domain = get_current_site(request).domain
    context = {
        'event_template': Event.objects.get(pk=event_template_id),
        'domain': domain
    }
    return render(request, template_name, context)

@login_required
def edit_event_template(request, event_template_id):
    '''View to handle updating an event template

    Arguments:
        request {object} -- http request object
        event_template_id {int} -- event object id

    Returns:
        render -- If request method is GET then it renders the form populated with the data from the event instance
        if the request is a POST then it performs the proper updates and renders the event details view.
    '''

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

                return HttpResponseRedirect(reverse('volunteer:event_template_details', args=(event_template_id,)))

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

                return HttpResponseRedirect(reverse('volunteer:event_template_details', args=(event_template_id,)))
            else:
                template_name = "events/new_event_template.html"
                return render(request, template_name, {"new_event_form": new_event_form})

@login_required
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return HttpResponseRedirect(reverse('volunteer:dashboard'))

@login_required
def delete_event_confirm(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, "events/delete_confirm.html", {'event': event})

@login_required
def schedule_event(request, event_template_id):
    '''Handles the calendar view for users to schedule event occurences

    Arguments:
        request {object} -- http response object
        event_template_id {int} -- event object id

    Returns:
        render -- returns calendar view for users to select days to schedule. If request method is a post
        then it returns a redirect to the dashboard after scheduling the event occurences.
    '''

    calendars = create_calendars()
    event = Event.objects.get(pk=event_template_id)
    scheduled_events = Event.objects.filter(name=event.name)

    # TODO: org cookies?
    org = Organization.objects.filter(user=request.user)[0]
    if request.method == "GET":
        template_name = "events/schedule_event.html"
        context = {
            "org": org,
            "event":event,
            'calendars': calendars,
            'scheduled_events':scheduled_events
        }

        return render(request, template_name, context)

    elif request.method == "POST":
        form_data = request.POST

        event_form_data = {
            'event': event,
            'date': form_data.getlist('selected_date'),
        }

        # Schedule Events

        for date in event_form_data['date']:
            scheduled_event = Event.objects.create(
                organization=org,
                name=event.name,
                description=event.description,
                venue=event.venue,
                date=date,
                is_template=False
            )

            shift_templates = Shift.objects.filter(event=event)

            # Schedule all appropriate shifts
            for template in shift_templates:
                Shift.objects.create(
                    start_time=template.start_time,
                    end_time=template.end_time,
                    num_volunteers=template.num_volunteers,
                    description=template.description,
                    event=scheduled_event
                )

    return HttpResponseRedirect(reverse('volunteer:dashboard'))


def create_calendars():
    '''returns a calender object with 13 months.
    Starting with the current month and only going to future months

    Returns:
        calender -- object with indexes 0 through 12. with 0 being the current month and 12 being the current month of the next year.
    '''

    now = datetime.datetime.now()
    month_current_year = 0
    months_remaining = 12 - now.month
    calendars = OrderedDict()

    # generate future months this year
    while month_current_year <= months_remaining:
        cal = month_cal(year=now.year, month=now.month, month_iter=month_current_year)
        calendars["{0}".format(month_current_year)] = mark_safe(cal)
        month_current_year += 1

    # generate the remainder from the next year to total 12 months
    month_next_year = 0
    additional_months = month_current_year - 1
    while month_next_year < 12 - additional_months:
        cal = month_cal(year=now.year + 1, month = 1, month_iter=month_next_year)
        calendars["{0}".format(month_current_year)] = mark_safe(cal)
        month_current_year +=1
        month_next_year += 1

    return calendars

