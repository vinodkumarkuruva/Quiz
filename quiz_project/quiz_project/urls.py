from django.contrib import admin
from django.urls import path, include
from quiz.views import start_quiz

urlpatterns = [
    path('', start_quiz, name='start'),
    path('admin/', admin.site.urls),
    path('quiz/', include('quiz.urls')),
]
