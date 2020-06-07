# Create your views here.
from django.shortcuts import render, redirect

from webapp.models import Task
from webapp.forms import SignUpForm,TaskForm

from datetime import date

from django.contrib.auth import login, authenticate

def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user-home')
    else:
        form = SignUpForm()
    return render(request, 'index.html',{'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user-home')
    else:
        form = SignUpForm()
    return render(request, 'webapp/signup.html', {'form': form})

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

class user_home(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Task

    template_name ='webapp/user_home.html'
    
    def get_queryset(self): 
        
        query = self.request.GET.get('q')
        status = self.request.GET.get('status')
        label = self.request.GET.get('label')
        due_date = self.request.GET.get('due_date')

        result=Task.objects.filter(user=self.request.user)
        if query :
            result=result.filter(Q(name__icontains=query))
        if status:
            result=result.filter(Q(status__icontains=status))
        if label:
            result=result.filter(Q(label__icontains=label))
        if due_date:
            result=result.filter(due_date__range=[date.today(),due_date])
            
        return result

class taskDetailView(LoginRequiredMixin,generic.DetailView):
    model = Task


from django.views.generic.edit import CreateView, UpdateView, DeleteView

class taskCreate(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date_created = date.today()
        return super().form_valid(form)


class taskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date_created = date.today()
        return super().form_valid(form)

class taskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    fields = '__all__'

from django.shortcuts import (HttpResponse, render, redirect,
                        get_object_or_404, reverse, get_list_or_404, Http404)

from django.contrib.auth.models import User

def profile(request):
    user = get_object_or_404(User, username=request.user.username)
 
    if request.user.username != user.username:
        raise Http404
 
    return render(request, 'webapp/profile.html',{'user' : user} )
''' 
from rest_framework import viewsets
from rest_framework import filters
from .serializers import TaskSerializer

class TaskViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    search_fields =['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Task.objects.all().order_by('name')
    serializer_class = TaskSerializer

    def get_queryset(self): 
        
        query = self.request.GET.get('search')
        status = self.request.GET.get('status')
        #label = self.request.GET.get('label')
        #due_date = self.request.GET.get('due_date')

        if query is None:
            return Task.objects.filter(user=self.request.user)

        return Task.objects.filter(Q(name__icontains=query) & Q(status__icontains=status) )
'''