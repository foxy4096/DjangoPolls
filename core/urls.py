from django.urls import path

from . import views

namespace="core"
urlpatterns = [
    path("", views.redirect_to_poll, name="redirect_to_polls"),
    path("profile/", views.profile, name="profile"),
    path("signup/", views.UserCreateView.as_view(), name="signup"),
]