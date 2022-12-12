from django.shortcuts import render

import random
import string


def main(request):
    return render(request, 'generator/main.html', context={'range': range(6, 21)})


def password(request):
    characters = list(string.ascii_lowercase)
    length = int(request.GET.get('length', 8))
    password_parameters = {
        'uppercase': string.ascii_uppercase,
        'numbers': string.digits,
        'special': string.punctuation,
    }
    for parameter, value in password_parameters.items():
        if request.GET.get(parameter):
            characters.extend(value)

    the_password = ''
    for char in range(length):
        the_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html')
