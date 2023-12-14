from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('test_rest/', include('restaurant_api.urls')),
]
