from django.urls import path
from . import views


urlpatterns = [
   path("",views.index,name='shopHome'),
   path("about",views.about,name='shopAbout'),
   path("checkout",views.checkout,name='shopCheckout'),
   path("contact",views.contact,name='shopContact'),
   path("products/<int:myid>",views.productview,name='ShopProdView'),
   path("search",views.search,name='ShopSearch'),
   path("tracker",views.tracker,name='trackerShop')
]