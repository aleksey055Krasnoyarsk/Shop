from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# Create your views here.
from .models import Post
from .models import About_us
from .models import Glavnaya
from .models import Contacts

def index(request):
    return render(request, 'blog/index.html', {})


def glavnaya(request):
    glav = get_object_or_404(Glavnaya)
    return render(request, 'blog/glavnaya.html', {'glav': glav})




def about_us(request):
    about = get_object_or_404(About_us)
    return render(request, 'blog/about_us.html', {'about': about})




def contacts(request):
    cont = get_object_or_404(Contacts)
    return render(request, 'blog/contacts.html', {'cont': cont})






def news(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/news_list.html', {'posts': posts})

def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/news_detail.html', {'post': post})