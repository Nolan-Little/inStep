from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization, Event

def dashboard(request):
    user = request.user
    org = Organization.objects.get(user=user)
    events = Event.objects.filter(organization=org)
    templates = events.filter(is_template=True)
    scheduled_events = events.exclude(date__lt=datetime.now()).exclude(date=None)

    context = {
        "org": org,
        "event_templates": templates,
        "scheduled_events": scheduled_events
    }

    return render(request, "dashboard.html", context)

