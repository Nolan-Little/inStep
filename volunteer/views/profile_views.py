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
        user = request.user
        data = request.POST
        form_data = {
            'username': data['username'],
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['email'],
            'org_name': data['org_name'],
            'org_description': data['org_description']
        }

        edit_profile_form = EditProfileForm(data=form_data)
        if form_data['username'] != request.user.username:
            edit_profile_form.clean_edit_username()

        if edit_profile_form.is_valid():
            template_name = "profile/profile.html"
            context = {
                'org': org
            }
            User.objects.filter(pk=user.id).update(
                username = data['username'],
                first_name =  data['first_name'],
                last_name = data['last_name'],
                email = data['email']
            )
            Organization.objects.filter(pk=org.id).update(
                name = data['org_name'],
                description = data['org_description']
                )
        else:
            template_name = "profile/edit_profile.html"
            context = {
                'org': org,
                'edit_form': edit_profile_form
            }


    return render(request, template_name, context)
