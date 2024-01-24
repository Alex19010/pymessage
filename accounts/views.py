from django.shortcuts import render, redirect

from .models import User
from .form import UserRegistrationForm


def home(request):
    return render(request, 'home.html')

def support(request):
    return render(request, 'support.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def register(request): 
    form = UserRegistrationForm() # Определяется пустая форма для регистрации пользователя
 
    if request.method == "POST": # Если пользователь ввёл данные в html форму и отправил их на сервер
        form = UserRegistrationForm(data=request.POST) # передаём данные в форму
        if form.is_valid(): # форма проверяет данные
            user = User.objects.create( # создаём пользователя
                username = form.cleaned_data['username'], # передаём пользователю username
                email = form.cleaned_data['email'], # передаём пользователю email
            )
            user.set_password(raw_password=form.cleaned_data['password']) # хешируем пароль пользователя
            user.save() # сохранение пользователя
            return redirect("accounts:login") # перенаправление пользователя на страницу авторизации
    

    context = { # определение контекса
        "form": form
    }
    # отправка контекстных данных на html шаблон
    return render(request=request, template_name="register.html", context=context)



def test(request):
    return render(request, 'main_home.html')