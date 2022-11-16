from django.urls import path

from pages import views

urlpatterns = [
    path('success', views.response_200, name='success'),
    path('forbidden', views.response_403, name='forbidden'),
    path('redirect', views.response_302, name='redirect'),
]
