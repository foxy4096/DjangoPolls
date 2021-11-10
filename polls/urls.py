from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('',  views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='question'),
    path('result/<int:pk>/', views.ResultView.as_view(), name='result'),
    path('vote/', views.vote, name='vote'),
]   