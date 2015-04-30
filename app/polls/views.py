from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    # output = ", ".join([p.question_text for p in latest_questions])
    context = {'latest_questions': latest_questions, 'name': "Ferdi Ramdhon"}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question with id {} does not exist.".format(question_id))
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "You're voting on question {}".format(question_id)
    return HttpResponse(response)
