# quiz/urls.py
from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('show_all/', views.show_all_questions, name='show_all_questions'),  
    path('submit/', views.submit_answer, name='submit_answer'),  
    path('results/', views.results, name='results'),

    # Extra urls - 
    # path('question/', views.get_random_question, name='get_random_question'),
    # path('add/', views.add_question, name='add_question'),
]
