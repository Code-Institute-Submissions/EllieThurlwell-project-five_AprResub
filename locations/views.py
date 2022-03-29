from django.shortcuts import render

from .models import Location

# Create your views here.


def all_locations(request):
    """ view to render locations page """
    locations = Location.objects.all()

    context = {
        'locations': locations
    }

    return render(request, 'locations/locations.html', context)
