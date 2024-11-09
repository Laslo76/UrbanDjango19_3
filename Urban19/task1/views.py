from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Contactform
from django.http import HttpResponse
from .models import Buyer, Game

class MainPage(TemplateView):
    template_name = './first_task/index.html'


class Basket(TemplateView):
    template_name = './first_task/basket_templates.html'


class Shop(TemplateView):
    def get(self, request):
        template = './first_task/shop_template.html'
        products = [{'name': _.title,
                     'description': _.description,
                     'cost': _.cost} for _ in Game.objects.all()]
        context = {'products': products}
        return render(request, template, context)


def sign_up_by_django(request):
    template_name = './first_task/registration_page.html'
    info = {}
    users = {u.name: {'balance': u.balance, 'age': u.age} for u in Buyer.objects.all()}
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, template_name=template_name, context=info)
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18 лет'
                return render(request, template_name=template_name, context=info)
            if username not in users.keys():
                Buyer.objects.create(name=username,
                                     balance=0,
                                     age=age)
            info = {'username': username}
            template_name = './first_task/index.html'
            return render(request, template_name=template_name, context=info)
    else:
        form = Contactform()
    return render(request, template_name, {'form': form})
