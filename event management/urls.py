from django.urls import path
from . import views
from .views import event_list
from .views import create_event

urlpatterns = [
    path('', event_list, name='home'),
    path('views.event_list', event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/register/', views.register, name='register'),
    path('event/create/', create_event, name='create_event'),
]
