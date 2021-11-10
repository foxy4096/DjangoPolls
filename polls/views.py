from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import Choice, Question



class HomeView(LoginRequiredMixin, generic.ListView):
    """
    A class based view to show the question on the homepage
    """
    model = Question
    context_object_name = "questions"
    template_name = "polls/home.html"



class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
    """
    A class based view to get detail about the question
    """
    model = Question
    template_name = "polls/question_detail.html"



class ResultView(LoginRequiredMixin, generic.DetailView):
    """
    Show result of the specific question
    """
    model = Question
    template_name = "polls/result_detail.html"



@login_required
def vote(request):
    """
    A function based view to add vote to a specific question
    """
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
