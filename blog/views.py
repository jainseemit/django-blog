from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
from django.views.generic import ListView,DetailView, CreateView
from .models import Post

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(CreateView):
    model=Post
    template_name = 'addblog.html'
    fields = '__all__'

def addBlog(request):
    form=blogForm()
    if request.method=='POST':
        form=blogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
    }
    return render(request,'addblog.html',context)