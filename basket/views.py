from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ view to render contents of the basket page """

    return render(request, 'basket/basket.html')
