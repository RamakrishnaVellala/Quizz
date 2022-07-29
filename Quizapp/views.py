from unicodedata import category
from urllib import response
from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import requests
from django.contrib import messages
from .serializers import QuestionSerializer
from .forms import createuserform, addQuestionform
from django.contrib.auth.forms import AuthenticationForm
from django_filters.rest_framework import DjangoFilterBackend
from .models import *


class QuizViewSet(viewsets.ModelViewSet):
    queryset = QuesForm.objects.all().order_by('id')
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


def home(request):
    categories = Category.objects.all()
    if request.GET.get('category'):
        return redirect(f" /quizz/?category={request.GET.get('category')} ")
    return render(request, 'home.html', {'categories': categories})


def quizz(request):
    response = requests.get('http://127.0.0.1:8000/api/quiz').json()
    categories = Category.objects.all()

    return render(request, 'quiz.html', {'response': response, 'categories': categories})


def register(request):
    if request.method == 'POST':
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
        messages.success(
            request, f'Your account has been created! You are now able to log in')
        return redirect('login')
    else:
        form = createuserform()
    return render(request, 'register.html', {'form': form, 'title': 'reqister here'})


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f" wecome {username} !!")
            return redirect('home')
        else:
            messages.info(request, f" account does not exit plz sign in")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})


def Logout(request):
    logout(request)
    return redirect('home')


def addQuestion(request):
    if request.user.is_staff:
        form = addQuestionform()
        if(request.method == 'POST'):
            form = addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'addQuestion.html', context)
    else:
        return redirect('home')
