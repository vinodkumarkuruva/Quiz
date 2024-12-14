from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, QuizSession
from django.shortcuts import get_object_or_404
from .forms import QuestionForm
import random


def start_quiz(request):
    session = QuizSession.objects.create(total_questions=0, correct_answers=0, incorrect_answers=0)
    request.session['session_id'] = session.id
    questions = list(Question.objects.all())
    # random.sample(questions, min(len(questions), 10))
    selected_questions = questions
    question_ids = [question.id for question in selected_questions]
    request.session['question_ids'] = question_ids
    # print(request.session['question_ids'])
    # print(question_ids)
    return render(request, 'quiz/start.html', {'questions': selected_questions})
    # return render(request, 'quiz/start.html')


def show_all_questions(request):
    questions = Question.objects.all()
    return render(request, 'quiz/all_questions.html', {'questions': questions})


def submit_answer(request):
    if request.method == 'POST':
        session_id = request.session.get('session_id')
        if not session_id:
            return HttpResponse("No session found. Please start a new quiz session.")
        session = get_object_or_404(QuizSession, id=session_id)
        question_ids = request.session.get('question_ids', [])
        if not question_ids:
            return HttpResponse("Error: No questions found for this session.")
        answers = {}
        dic1 = dict(request.POST)
        print(dic1)
        for question_id in question_ids:
            print(question_id)
            answer_key = f'answer_{question_id}'
            answer_list = dic1.get(answer_key, [])
            if answer_list:  # Ensure an answer exists
                answers[question_id] = answer_list[0]
            else:
                return HttpResponse(f"Error: Missing answer for question {question_id}.")
        print(answers)
        score = 0
        for question_id, user_answer in answers.items():
            question = get_object_or_404(Question, id=question_id)
            if str(user_answer).strip().lower() == str(question.correct_option).strip().lower():
                score += 1
        # Update QuizSession with results
        session.total_questions = len(question_ids)
        session.correct_answers = score
        session.incorrect_answers = len(question_ids) - score
        session.save()
        return redirect('quiz:results')
    else:
        return HttpResponse("Invalid request method.")


def results(request):
    session_id = request.session.get('session_id')
    if not session_id:
        return HttpResponse("No session found. Please start a new quiz session.")

    session = get_object_or_404(QuizSession, id=session_id)
    return render(request, 'quiz/results.html', {'session': session})


# End for Creating Questions -------- Optional 

# def add_question(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             if Question.objects.count() >= 10:
#                 return redirect('quiz:show_all_questions')
#             return render(request, 'quiz/add_question.html', {'form': form})
#     else:
#         form = QuestionForm()
#     return render(request, 'quiz/add_question.html', {'form': form})




# This endpoint randomly getting questions rom list of question in quiz -------

# def get_random_question(request):
#     questions = Question.objects.all()
#     session_id = request.session.get('session_id')
#     if not session_id:
#         return redirect('quiz:start_quiz')

#     if questions.exists():
#         question = random.choice(questions)
#         request.session['question_ids'] = request.session.get('question_ids', []) + [question.id]
#         return render(request, 'quiz/question.html', {'question': question})
#     else:
#         return HttpResponse("No questions available at the moment. Please start a new quiz session.")
