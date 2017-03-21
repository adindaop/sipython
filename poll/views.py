from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

def index(request):
    context = {} #inisialisasi harus kosong
    questions_query = Question.objects.all() #questions_query = variabel
    context['questions'] = questions_query #yg di tanda '' boleh beda dr variabel
    return render(request, 'poll/index.html', context)

def help_me(request):
    context = {}
    return render(request, 'poll/help_me.html', context)

def detail_question(request, question_id):
    context = {}
    question = Question.objects.get(id=question_id)
    context['question'] = question
    return render(request, 'poll/detail_question.html', context)

def vote(request):
    context = {}
    choice_id = request.POST['choice']
    selected_choice = Choice.objects.get(id=int(choice_id))
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('poll:results', args=(selected_choice.question.id,)))

def results(request, question_id):
    context = {}
    question = Question.objects.get(pk=question_id)
    return render(request, 'poll/results.html', {'question': question})
