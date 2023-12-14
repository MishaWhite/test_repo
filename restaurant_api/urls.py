from django.urls import path

from restaurant_api import views

app_name = 'restaurant_api'

urlpatterns = [
    path('get_human_hours/', views.RestHoursView.as_view()),
]
