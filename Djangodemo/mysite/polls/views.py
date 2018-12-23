from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
# Create your views here.

def index(request):
    latestQuestions = Question.objects.order_by('-pub_date')[:5] #- is important here
    context = {
        'latestQuestions':latestQuestions
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selectedChoice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question': question, 'error_message':"Please select a choice"})
    else:
        selectedChoice.votes+=1
        selectedChoice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))