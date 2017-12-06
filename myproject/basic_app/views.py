from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (TemplateView,ListView,
DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'basic_app/base.html')

class UserContactListView(ListView):
    model = User
    template_name = "basic_app/usercontact_list.html"

class USerContactDetailView(DetailView):
    model = User
    template_name = "basic_app/usercontact_detail.html"    
