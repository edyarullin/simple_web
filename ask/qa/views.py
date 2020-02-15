from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django.contrib.auth import login

from .models import Question
from .forms import AskForm, AnswerForm, SignupForm, LoginForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        num_page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(num_page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', {
        'form': form,
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')

    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {
        'form': form,
    })


@require_GET
def new_questions(request):
    questions = Question.objects.new()
    page, paginator = paginate(request, questions)
    paginator.baseurl = reverse('qa-main')
    return render(request, 'qa/questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def popular_questions(request):
    questions = Question.objects.popular()
    page, paginator = paginate(request, questions)
    paginator.baseurl = reverse('qa-popular')
    return render(request, 'qa/questions.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question_details(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form.set_fields(request.user, question)
        if form.is_valid():
            model = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AnswerForm()
        form.set_fields(request.user, question)
    return render(request, 'qa/question_details.html', {
        'question': question,
        'answers': question.answer_set.all(),
        'form': form
    })


def ask_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form.set_user(request.user)
        if form.is_valid():
            model = form.save()
            return HttpResponseRedirect(model.get_url())
    else:
        form = AskForm()
        form.set_user(request.user)
    return render(request, 'qa/ask.html', {
        'form': form,
    })
