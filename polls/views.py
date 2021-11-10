from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Choice, Question
# Create your views here.

class HomeView(LoginRequiredMixin, generic.ListView):
    model = Question
    context_object_name = "questions"
    template_name = "polls/home.html"


class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = "polls/question_detail.html"

class ResultView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = "polls/result_detail.html"

@login_required
def vote(request):
    try:
        choice = Choice.objects.get(pk=request.POST.get('choice'))
        question = Question.objects.get(choice=choice)
        if request.user in question.voted.all():
            return redirect("polls:question", question.pk)
        else: 
            question.voted.add(request.user)
            choice.votes = choice.votes + 1
            question.save()
            choice.save()
            return redirect("polls:result", question.pk)
    except:
        return redirect('polls:home')
