from . import views
from django.urls import path,include
from customer_portal.views import *
# from django.conf.urls import url
urlpatterns = [
    path('index/',views.index),
    path('login/',views.login),
    path('auth/',views.auth_view),
    path('logout/',views.logout_view),
    path('register/',views.register),
    path('registration/',views.registration),
    path('search/',views.search),
    path('search_results/',views.search_results),
    path('rent/',views.rent_vehicle),
    path('confirmed/',views.confirm),
    path('manage/',views.manage),
    path('update/',views.update_order),
    path('delete/',views.delete_order),
]