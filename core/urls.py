from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_poll),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.UserCreateView.as_view(), name='signup'),
]