from django.urls import path
from .views import Index, listing, search


urlpatterns = [

    path('',Index, name='listings'),
    path('<int:listing_id>',listing, name='listing'),
    path('search',search, name='search'),

]


