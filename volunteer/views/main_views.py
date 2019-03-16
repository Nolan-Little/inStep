from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization




# Create your views here.

def index(request):
'''auth layer

Arguments:
    request {object} -- http request

Returns:
    render -- if user is not authenticated directs to landing page where they can login or register
    if user is authenticated directs to new org page if they don't have one associated or to dashboard
'''

    if request.user.is_authenticated:
        try:
            org = Organization.objects.get(user=request.user)
            return HttpResponseRedirect(reverse('volunteer:dashboard'))
        except Organization.DoesNotExist:
            return HttpResponseRedirect(reverse('volunteer:new_org'))
    else:
        template_name = 'auth/landing_page.html'
        context = {}

    return render(request, template_name, context)