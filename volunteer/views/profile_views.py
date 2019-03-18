import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization
from volunteer.forms import EditProfileForm


def profile(request):
    '''read user profile

    Arguments:
        request {request} -- http request object
    '''
    # TODO: change org to selection
    org = Organization.objects.filter(user=request.user)[0]
    template_name = "profile/profile.html"
    context = {
        'org': org
    }
    return render(request, template_name, context)

def edit_profile(request):
    # TODO: change org to selection
    org = Organization.objects.filter(user=request.user)[0]


    if request.method == "GET":
        user = request.user
        data = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'org_name': org.name,
            'org_description': org.description
        }

        edit_profile_form = EditProfileForm(data=data)
        template_name = "profile/edit_profile.html"
        context = {
            'org': org,
            'edit_form': edit_profile_form
        }


    if request.method == "POST":
        pass

    return render(request, template_name, context)
