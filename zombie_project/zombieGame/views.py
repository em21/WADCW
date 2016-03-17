from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "zzzzz"}
    return render(request, 'zombieGame/index.html', context_dict)


def login(request):
    context_dict = {'boldmessage': "login"}
    return render(request, 'zombieGame/login.html', context_dict)

def profile(request):
    context_dict = {'boldmessage': "profile"}
    return render(request, 'zombieGame/profile.html', context_dict)

def game(request):
    context_dict = {'boldmessage': "game"}
    return render(request, 'zombieGame/game.html', context_dict)

def leaderboard(request):
    context_dict = {'boldmessage': "leaderboard"}
    #kills_list = kills.objects.order_by('-kills')[:10]
    #survival_list = survival.objects.order_by('-days')[:10]
    return render(request, 'zombieGame/leaderboard.html', context_dict)

