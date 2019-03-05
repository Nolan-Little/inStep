from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization, EventTemplate, ScheduledEvent
from volunteer.forms import EventTemplateForm


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
            EventTemplate.objects.create(
                name=event_form_data['name'],
                description=event_form_data['description'],
                venue=event_form_data['venue'],
                location=event_form_data['location'],
                organization=org
            )
            return HttpResponseRedirect(reverse('volunteer:dashboard'))

        else:
            template_name = 'events/new_event_template.html'
            return render(request, template_name, {'new_event_form': new_event_form})


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
        print(form_data)
        event_form_data = {
            'event': form_data['events'],
            'date': form_data['date'],
        }

        event = org.eventtemplate_set.filter(pk=event_form_data['event'])[0]

        ScheduledEvent.objects.create(
            date=event_form_data['date'],
            event_template=event
        )
    return HttpResponseRedirect(reverse('volunteer:dashboard'))


def sign_up(request, unique_url):
    template_name = "events/sign_up.html"
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=", unique_url)
    context = {
        'scheduled_event': ScheduledEvent.objects.get(sign_up_url=unique_url)
    }
    return render(request, template_name, context)