from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from volunteer.models import Organization

def dashboard(request):
    user = request.user
    org = Organization.objects.get(user=user)


    context = {
        "org": org
    }

    return render(request, "dashboard.html", context)
