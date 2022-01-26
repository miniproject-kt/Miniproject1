# from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Posting
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Create your views here.

def main(request):
    return render(request, 'postapp/blog.html')

def category(request):
    post_list = Posting.objects.all()
    return render(request, 'postapp/category.html', {'post_list' : post_list})



def form_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.user_id = 1
            posting.save()
            
        return redirect('/postapp/category/')
    else:
        form = PostForm()

    return render(
        request, 'postapp/form_post.html', {'form' : form}
    )



def detail(request, pk):
    result = get_object_or_404(Posting, l_posting_index = pk)
    context = {'result' : result}
    return render(request, 'postapp/post_detail.html', context)

