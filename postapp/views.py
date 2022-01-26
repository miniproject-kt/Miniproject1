# from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Posting
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def main(request):
    return render(request, 'postapp/blog.html')

def category(request):
    now_page =int(request.GET.get('page', 1))
    post_list = Posting.objects.order_by('-l_posting_index')
                # 포스트 , 보여줄 게시글 개수
    p = Paginator(post_list, 3)
    info = p.get_page(now_page)

    start_page = (now_page - 1) // 3 * 3 + 1
    end_page = start_page + 3
    if end_page > p.num_pages:
        end_page = p.num_pages

    # 페이지 마지막 번호
    last_page_num = 0
    for last_page in p.page_range:
        last_page_num = last_page + 1



    context = {
        'info' : info,
        'page_range' : range(start_page, end_page+1),
        'now_page' : now_page
    }
    return render(request, 'postapp/category.html', context)



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

