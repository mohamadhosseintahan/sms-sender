from django.shortcuts import render
from django.views.generic import ListView , CreateView , UpdateView , DeleteView , DetailView
from Base.models import Message
from .forms import SMSForm
from django.urls import reverse_lazy
# Create your views here.

class MessageList(ListView):
    model = Message
    paginate_by = 15
    template_name = 'list.html'
    context_object_name = 'messages'

class MessageCreate(CreateView):
    model = Message
    form_class = SMSForm
    # fields = ('receptor' , 'message' ,)
    template_name = 'form.html'
    success_url = reverse_lazy('list')

class MessageDetail(DetailView):
    model = Message
    template_name = 'detail.html'
    context_object_name = 'message'

class MessageUpdate(UpdateView):
    model = Message
    form_class = SMSForm
    # fields = ('receptor' , 'message' ,)
    template_name = 'form.html'
    success_url = reverse_lazy('list')

class MessageDelete(DeleteView):
    model = Message
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
    context_object_name = 'message'
