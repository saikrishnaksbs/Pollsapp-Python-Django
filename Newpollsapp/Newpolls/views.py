from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect

from .models import Question, Choice

from django.urls import reverse

import datetime

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    a=Question.objects.all().values()
    print(a)
    context = {'latest_question_list': latest_question_list}
    return render(request, '/home/saikrishna/Django/Newpollsapp/Newpolls/templates/Newpoll/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, '/home/saikrishna/Django/Newpollsapp/Newpolls/templates/Newpoll/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, '/home/saikrishna/Django/Newpollsapp/Newpolls/templates/Newpoll/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, '/home/saikrishna/Django/Newpollsapp/Newpolls/templates/Newpoll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('Newpolls:results', args=(question.id,)))

