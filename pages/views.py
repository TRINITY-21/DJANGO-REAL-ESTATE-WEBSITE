from django.shortcuts import render,get_object_or_404
from listings.models import Listings
from listings.choices import price_choices, bedroom_choices,state_choices

def Index(request):
    listings = Listings.objects.order_by('-list_date').filter(is_published=True)


    context = {'listings': listings,
                    'state_choices': state_choices,
                    'bedroom_choices': bedroom_choices,
                    'price_choices':price_choices,
    }
    return render(request, 'pages/index.html', context)


def About(request):
    return render(request, 'pages/about.html')
