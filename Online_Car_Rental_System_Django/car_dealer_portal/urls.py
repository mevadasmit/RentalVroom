from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('login/',views.login),
    path('auth/',views.auth_view),
    path('logout/',views.logout_view),
    path('register/',views.register),
    path('registration/',views.registration),
    path('add_vehicle/',views.add_vehicle),
    path('manage_vehicles/',views.manage_vehicles),
    path('order_list/',views.order_list),
    path('complete/',views.complete),
    path('history/',views.history),
    path('delete/',views.delete),
]