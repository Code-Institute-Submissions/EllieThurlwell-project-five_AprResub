from django.shortcuts import render

# Create your views here.


def locations(request):
    """ view to render locations page """

    return render(request, 'locations/locations.html')
