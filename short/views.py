from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseNotFound

from short.models import Link
from short.forms import LinkForm
import pyshorteners
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            if not Link.objects.filter(link=form.cleaned_data.get('link'),user=request.user).exists():
            # form.save()
            # print(form.cleaned_data.get('link'))
                Link.objects.create(link=form.cleaned_data.get('link'), shortlink=pyshorteners.Shortener().clckru.short(form.cleaned_data.get('link')), user=request.user)
                return HttpResponseRedirect('/')
            else:
                # pass
                exists = 'y'
            response = {
                'exists': exists
            }
            return JsonResponse(response)

    form = LinkForm()

    links = Link.objects.filter(user=request.user.id)

    data = {
        'form': form,
        'links': links,
        # 'exists': exists
    }
    return render(request, 'index.html', data)

def registration(request):
    return render(request, 'registration.html')

def registr(request):
    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email']
    )
    login(request, user)
    return HttpResponseRedirect('index')

def back(request):
    return HttpResponseRedirect('/')

def login_users(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, 'error.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('/')

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')

def delete(request, id):
    try:
        link_obj = Link.objects.get(id=id)
        link_obj.delete()
        return HttpResponseRedirect('/')
    except Link.DoesNotExist:
        return HttpResponseNotFound('<h2>Money not found</h2>')

def login_1(request):
    if len(User.objects.filter(username=request.POST['aaa'])) == 0:
        exists = 'n'
    else:
        exists = 'y'
    response = {
        'exists': exists
    }
    return JsonResponse(response)