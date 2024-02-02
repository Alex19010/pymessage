from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

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


def register_up(request): 
    form = UserRegistrationForm() # Определяется пустая форма для регистрации пользователя
 
    if request.method == "POST": # Если пользователь ввёл данные в html форму и отправил их на сервер
        form = UserRegistrationForm(data=request.POST) # передаём данные в форму
        if form.is_valid(): # форма проверяет данные
            user = User.objects.create( # создаём пользователя
                first_name = form.cleaned_data['first_name'], # передаём пользователю username
                last_name = form.cleaned_data['last_name'],
                date_of_birth = form.cleaned_data['date_of_birth'],
                email = form.cleaned_data['email'], # передаём пользователю email
                address = form.cleaned_data['address'],
            )
            user.set_password(raw_password=form.cleaned_data['password']) # хешируем пароль пользователя
            user.save() # сохранение пользователя
            login(request, user)
            return redirect("home") # перенаправление пользователя на страницу авторизации
    
    context = { # определение контекса
        "form": form
    }
    # отправка контекстных данных на html шаблон
    return render(request=request, template_name="register_up.html", context=context)


def register_in(request):
    if request.method == "POST": # получаем POST запрос с его данными
        email = request.POST.get("email") # достаём из запроса username
        password = request.POST.get("password") # достаём из запроса password
        user = authenticate(request, username=email, password=password) # проверяем username и password на существование
        if user is not None: # Если пользователь с таким username и password найден
            login(request, user) # авторизуем пользователя
            return redirect("home") # перенаправляем его на главную страницу
        
        context = {
            "error": "Ошибка! Проверьте username и password!"
        }
        return render(request=request, template_name="register_in.html", context=context)
    return render(request=request, template_name="register_in.html")


def logout_view(request):
    logout(request)
    return redirect('home')


# def register_in(request):
#     return render(request, 'register_in.html')

# def register_up(request):
#     return render(request, 'register_up.html')



# def test(request):
#     return render(request, 'main_home.html')