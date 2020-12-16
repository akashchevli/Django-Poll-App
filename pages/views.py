from accounts.views import login
from typing import overload
from django.shortcuts import get_object_or_404, redirect, render
from user_poll.models import Questions, Voting
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    question = Questions.objects.all()
    user = request.user
 
    paginator = Paginator(question, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'question': page_obj,
        'user': user
    }
    if('/' == request.path):
        print(request.path)
        return render(request, 'pages/index.html', context)
    else:
        return render(request, 'pages/dashboard.html', context)

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return index(request)
    
    


