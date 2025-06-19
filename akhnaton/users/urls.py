from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('forbidden/',views.forbidden,name='forbidden'),
]