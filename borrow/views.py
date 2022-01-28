from django.http import HttpResponse
from django.shortcuts import render
from .models import Object, Borrower, User
from django.core.paginator import Paginator


def category(request):
    search_keyword = request.GET.get('post', '')
    post_list = Borrower.objects.all()
    if search_keyword:
        post_list = post_list.filter(title__contains=search_keyword)

    now_page =int(request.GET.get('page', 1))
    post_list = post_list.order_by('-b_posting_index')
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
    return render(request, 'borrow/category.html', context)






def getMap(request):

    if request.method == 'POST' and request.POST.get('stuff') != '':
        param = request.POST.get('stuff')

        stuffQuerySet = Object.objects.filter(object_name__contains=param)

        stuffs = []
        members = []
        posts = []
        for stuff in stuffQuerySet:

            stuffs.append(stuff)

            post = stuff.posting_index
            posts.append(post)

            member = post.lender_index
            members.append(member)


        data = {
            'members': members,
            'stuffs': stuffs,
            'posts': posts
        }

        return render(request, 'borrow/map.html', data)
    return render(request, 'borrow/map.html')
