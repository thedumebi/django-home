from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

"""def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(request, 'polls/index.html', context)"""

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

"""def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})"""

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

"""def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ctx = {'question': question}
    return render(request, 'polls/results.html', ctx)"""

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    ctx = {'question': question, 'error_message': "You didn't select a choice."}
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', ctx)
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))