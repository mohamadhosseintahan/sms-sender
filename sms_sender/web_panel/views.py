from django.shortcuts import render
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView
from Base.models import Message
from .forms import SMSForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MessageList( LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Message
    paginate_by = 15
    template_name = 'list.html'
    context_object_name = 'messages'

class MessageCreate(LoginRequiredMixin,CreateView):
    login_url = 'login'
    model = Message
    form_class = SMSForm
    template_name = 'form.html'
    success_url = reverse_lazy('tester')



class MessageDetail( LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Message
    template_name = 'detail.html'
    context_object_name = 'message'


class MessageDelete( LoginRequiredMixin,DeleteView):
    login_url = 'login'
    model = Message
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
    context_object_name = 'message'
