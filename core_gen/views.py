from django.shortcuts import render
#from django.http import HttpResponse
import random


def home(request):
    return render(request, "core_gen/home.html")


def password(request):
    characters = list('abcdefghijklmonpqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    gen_pwd = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('¬!"£$%^&*()<>/~}@:?'))


    for x in range(length):
        gen_pwd += random.choice(characters)

    return render(request, "core_gen/password.html", {'password': gen_pwd})


def about(request):
    return render(request, "core_gen/about.html")