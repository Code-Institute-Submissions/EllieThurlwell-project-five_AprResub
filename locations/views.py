from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Location
from .forms import LocationForm

# Create your views here.


def all_locations(request):
    """ view to render locations page """
    locations = Location.objects.all()

    context = {
        'locations': locations
    }

    return render(request, 'locations/locations.html', context)


@login_required
def add_location(request):
    """ view to handle the add location form from admin user """
    if not request.user.is_superuser:
        messages.error(request, 'Only admin users can access this page')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added location')
            return redirect(reverse('locations'))
        else:
            messages.error(request, 'Could not add location. Please try again')
    else:
        form = LocationForm()

    template = 'locations/add_location.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_location(request, location_id):
    """ view to handle the edit location form from admin user """
    if not request.user.is_superuser:
        messages.error(request, 'Only admin users can access this page')
        return redirect(reverse('home'))

    location = get_object_or_404(Location, pk=location_id)
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES, instance=location)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated location!')
            return redirect(reverse('locations'))
        else:
            messages.error(request, 'Update failed. Please try again')
    else:
        form = LocationForm(instance=location)
        messages.info(request, f'You are editing {location.location}')

    template = 'locations/edit_location.html'
    context = {
        'form': form,
        'location': location,
    }

    return render(request, template, context)


@login_required
def delete_location(request, location_id):
    """ view for admin to delete a location """
    if not request.user.is_superuser:
        messages.error(request, 'Only admin users can access this page')
        return redirect(reverse('home'))

    location = get_object_or_404(Location, pk=location_id)
    location.delete()
    messages.success(request, 'Location deleted')
    return redirect(reverse('locations'))
