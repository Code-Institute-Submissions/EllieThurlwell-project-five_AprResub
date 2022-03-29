from django.shortcuts import render

# Create your views here.


def contact(request):
    """ view to render contact page """

    return render(request, 'contact/contact.html')
