from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

from short.models import Link
from short.forms import LinkForm
import pyshorteners
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            if not Link.objects.filter(link=form.cleaned_data.get('link'), user=request.user).exists():
                Link.objects.create(link=form.cleaned_data.get('link'),
                                    shortlink=pyshorteners.Shortener().clckru.short(form.cleaned_data.get('link')),
                                    user=request.user)
                return HttpResponseRedirect('/')
            else:
                form = LinkForm()
                links = Link.objects.filter(user=request.user.id)
                data = {
                    'form': form,
                    'links': links,
                    'link_error': True
                }
                return render(request, 'index.html', data)
    form = LinkForm()
    links = Link.objects.filter(user=request.user.id)
    data = {
        'form': form,
        'links': links,
    }
    return render(request, 'index.html', data)


def login_p(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


def registr(request):
    if not User.objects.filter(username=request.POST['login']):
        if not User.objects.filter(email=request.POST['email']):
            user = User.objects.create_user(
                request.POST['login'],
                password=request.POST['password'],
                email=request.POST['email']
            )
            login(request, user)
            return HttpResponseRedirect('index')
        else:
            context = {'email_error': True}
            return render(request, 'registration.html', context)
    else:
        context = {'username_error': True}
        return render(request, 'registration.html', context)


def back(request):
    return HttpResponseRedirect('/')


def login_users(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )

    if user is None:
        context = {'username_error': True}
        return render(request, 'login.html', context)
    else:
        login(request, user)
        return HttpResponseRedirect('/')


def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')


def delete(request, id_link):
    try:
        Link.objects.get(id_link=id_link).delete()
        return HttpResponseRedirect('/')
    except Link.DoesNotExist:
        return HttpResponseNotFound('<h2>Link not found</h2>')
