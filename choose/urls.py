from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('organizer/', include('event_management.urls')),
    path('participant/', include('participant.urls'))
]