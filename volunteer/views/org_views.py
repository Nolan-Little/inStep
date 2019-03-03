from django.shortcuts import render
from django.contrib.auth.models import User
from volunteer.models import Organization
from volunteer.forms import NewOrgForm

def new_org(request, user_id):
    if request.method == "GET":
        template_name = "new_org.html"
        new_org_form = NewOrgForm()

        return render(request, template_name, {'new_org_form': new_org_form} )
    if request.method == "POST":
        print("WTF AM I NOT PRINTING", request.user.id)
        template_name='index.html'
        return render(request, template_name)
