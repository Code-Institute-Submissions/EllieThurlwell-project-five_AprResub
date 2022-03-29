from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm

# Create your views here.


def contact(request):
    """ view to render contact page """

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message sent!')

    contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
