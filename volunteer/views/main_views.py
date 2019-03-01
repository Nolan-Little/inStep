from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        if request.user.is_authenticated:
            # TODO: update to a dashboard.html that extends index
            template_name = 'index.html'
        else:
            template_name = 'auth/landing_page.html'
    except AttributeError:
        template_name = 'auth/landing_page.html'
    return render(request, template_name)