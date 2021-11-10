from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import SimplifiedUserChangeForm


def redirect_to_poll(request):
    """
    A function view which redirect the user from '/' to '/polls/'
    """
    return redirect("polls:home")



class UserCreateView(generic.FormView):
    """
    A class Based view to create a new user without any priviliages
    """
    form_class = UserCreationForm
    success_url = "/accounts/login"
    template_name = "core/User_create.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



@login_required
def profile(request):
    """
    A view to show user profile
    """
    if request.method == "POST":
        form = SimplifiedUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = SimplifiedUserChangeForm(instance=request.user)
        return render(request, "core/profile.html", {"form": form})
