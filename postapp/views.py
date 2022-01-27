# from http.client import HTTPResponse
from turtle import pos
from django.http import HttpResponse
from django.shortcuts import redirect, render
from sympy import Q
from .models import Posting, User, Lender_Chatting
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def main(request):
    return render(request, 'postapp/blog.html')

def category(request):
    search_keyword = request.GET.get('post', '')
    post_list = Posting.objects.all()
    if search_keyword:
        post_list = post_list.filter(title__contains=search_keyword)

    now_page =int(request.GET.get('page', 1))
    post_list = post_list.order_by('-l_posting_index')
                # 포스트 , 보여줄 게시글 개수
    p = Paginator(post_list, 6)
    info = p.get_page(now_page)

    # start_page = (now_page - 1) // 3 * 3 + 1
    # end_page = start_page + 3
    # if end_page > p.num_pages:
    #     end_page = p.num_pages

    # 페이지 마지막 번호
    last_page_num = 0
    for last_page in p.page_range:
        last_page_num = last_page + 1



    context = {
        'info' : info,
        'now_page' : now_page,
        'last_page_num' : last_page_num
    }
    return render(request, 'postapp/category.html', context)



def form_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            posting = form.save(commit=False)
            user = User.objects.get(user_id = request.session['user_id'])
            posting.user_id = user.user_index
            posting.save()
            
        return redirect('/postapp/category/')
    else:
        form = PostForm()

    return render(
        request, 'postapp/form_post.html', {'form' : form}
    )



def detail(request, pk):
    result = get_object_or_404(Posting, l_posting_index = pk)
    user = User.objects.get(user_index = result.user_id)
    comments = Lender_Chatting.objects.filter(posting_index = pk)
    context = {'result' : result, 'user' : user, 'comments' : comments}

    if request.method == 'POST':
        comment = Lender_Chatting()
        comment.user_id = user.user_id
        comment.user_index = user.user_index
        comment.chatting = request.POST['body']
        comment.posting_index = result.l_posting_index
        comment.save()

    return render(request, 'postapp/post_detail.html', context)


def edit(request, pk):
    posting = Posting.objects.get(l_posting_index = pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=posting)
        if form.is_valid():
            posting.save()
            return redirect('detail', pk = pk)
    else:
        form = PostForm(instance=posting)

    return render(
            request, 'postapp/post_edit.html', {'form':form, 'pk' : pk}
        )


def delete(request, pk):
    post = Posting.objects.get(l_posting_index = pk)
    post.delete()
    return redirect('/postapp/category')


