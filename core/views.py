from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import SimplifiedUserChangeForm
# Create your views here.

class UserCreateView(generic.FormView):
    """
    A class Based view to create a new user without any priviliages
    """
    form_class = UserCreationForm
    success_url = '/login'
    template_name = "core/User_create.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

def redirect_to_poll(request):
    return redirect('polls:home')

@login_required
def profile(request):
    if request.method == "POST":
        form = SimplifiedUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = SimplifiedUserChangeForm(instance=request.user)
        return render(request, 'core/profile.html', {'form': form})