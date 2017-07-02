from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from .models import Profile,Map
from .forms import UserForm,ProfileForm,MapForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

@login_required
def Home(request):
    return render(request, 'home/home.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'home/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class MapCreate(CreateView):
    model = Map
    fields=['map_name','map_data']

def create_map(request):
    form = MapForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        map = form.save(commit=False)
        map.save()
        return render(request, 'home/home.html')
    return render(request, 'home/home.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            map = form.save(commit=False)
            map.save()
            form.save()
            return redirect('index')
    else:
        form = MapForm()
    return render(request, 'home/map_create.html', {
        'form': form
    })

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
