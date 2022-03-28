from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ view to render the checkout page """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket right now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KiF2fGktD06S5XUJvh4hD88j6A08ui4n6Ty902qOSOFhSkW0kx49guph7CV7hya5Skvq2tKRNzoxWnPb2znoyj000dD01QyzE',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
