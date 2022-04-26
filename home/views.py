from django.shortcuts import render

# Create your views here.


def index(request):
    """ view to render index page """

    return render(request, 'home/index.html')


def admin_controls(request):
    """ view to render the admin page """

    return render(request, 'home/admin_controls.html')
