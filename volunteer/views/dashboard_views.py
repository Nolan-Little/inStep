from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization, EventTemplate, ScheduledEvent

def dashboard(request):
    user = request.user
    org = Organization.objects.get(user=user)
    event_templates = EventTemplate.objects.filter(organization=org)
    scheduled_events = ScheduledEvent.objects.all()

    for template in event_templates:
        scheduled_events.filter(event_template=template)

    context = {
        "org": org,
        "event_templates": event_templates,
        "scheduled_events": scheduled_events
    }

    return render(request, "dashboard.html", context)
