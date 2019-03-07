from datetime import datetime
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

    # last_login = days_since_login(request.user)
    # print(last_login)
    for template in event_templates:
        scheduled_events.filter(event_template=template)

    context = {
        "org": org,
        "event_templates": event_templates,
        "scheduled_events": scheduled_events
    }

    return render(request, "dashboard.html", context)


def days_since_login(user):
    last_login = user.last_login.strptime(str(user.last_login), "%Y-%m-%d")
    n = datetime.strptime(datetime.now(), "%Y-%m-%d")
    return abs((n - last_login).days)