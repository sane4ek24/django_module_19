from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse
from task1.models import Buyer, Game, News
from django.core.paginator import Paginator


def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        balance = request.POST.get('balance')
        age = int(request.POST.get('age'))

        existing_users = [buyer.name for buyer in Buyer.objects.all()]

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'

        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'

        elif name in existing_users:
            info['error'] = 'Пользователь с таким логином существует'

        else:
            Buyer.objects.create(name=name, balance=balance, age=age)
            return HttpResponse(f'Приветствуем, {name}')

    return render(request, 'registration_page.html', info)


def platform(request):
    return render(request, 'platform.html')


def cart(request):
    return render(request, 'cart.html')


def cases(request):
    title = 'Наличие игр'
    text = 'Ассортимент игр'
    game_list = Game.objects.all()
    context = {
        'title': title,
        'text': text,
        'game_list': game_list
    }
    return render(request, 'cases.html', context)


def news(request):
    posts = News.objects.all().order_by('date')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page_posts = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_posts': page_posts})
