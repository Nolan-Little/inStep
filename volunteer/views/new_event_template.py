from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization, EventTemplate
from volunteer.forms import EventTemplateForm


def new_event_template(request):
    if request.method == "GET":
        new_event_form = EventTemplateForm()
        template_name = "new_event_template.html"
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
                organization = org
            )
            return HttpResponseRedirect(reverse('volunteer:dashboard'))

        else:
            template_name = 'new_event_template.html'
            return render(request, template_name, {'new_event_form': new_event_form})


