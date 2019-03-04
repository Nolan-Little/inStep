from django.shortcuts import render
from django.contrib.auth.models import User
from volunteer.models import Organization
from volunteer.forms import NewOrgForm


def new_org(request):
    if request.method == "GET":
        template_name = "new_org.html"
        new_org_form = NewOrgForm()

        return render(request, template_name, {'new_org_form': new_org_form})
    if request.method == "POST":
        form_data = request.POST

        org_form_data = {
            'name': form_data['name'],
            'description': form_data['description']
        }

        new_org_form = NewOrgForm(org_form_data)
        if new_org_form.is_valid():
            new_org = Organization.objects.create(
                name=org_form_data['name'],
                description=org_form_data['description'],
            )

            new_org.user.add(request.user)
            context = {
                "org": new_org
            }

            template_name = 'index.html'
        else:
            template_name = 'new_org.html'
            return render(request, template_name, {'new_org_form': new_org_form})

        return render(request, template_name, context)
