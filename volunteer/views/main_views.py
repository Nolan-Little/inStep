from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization
from volunteer.forms import NewOrgForm




# Create your views here.

def index(request):
    if request.user.is_authenticated:
        try:
            org = Organization.objects.get(user=request.user)
            template_name = 'index.html'
            context = {'org': org}
        except Organization.DoesNotExist:
            return HttpResponseRedirect(reverse('volunteer:new_org', args=(request.user.id, )))
    else:
        template_name = 'auth/landing_page.html'
        context = {}

    return render(request, template_name, context)