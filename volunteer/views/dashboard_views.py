from datetime import datetime
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization, Event


@login_required
def dashboard(request):
    domain = get_current_site(request).domain
    user = request.user
    org = Organization.objects.get(user=user)
    events = Event.objects.filter(organization=org)
    templates = events.filter(is_template=True)
    scheduled_events = events.exclude(date__lt=datetime.now()).exclude(date=None).order_by('date')

    context = {
        "org": org,
        "event_templates": templates,
        "scheduled_events": scheduled_events,
        "domain": domain
    }

    return render(request, "dashboard.html", context)

