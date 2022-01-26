from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import app.models as models
from .models import User
from .models import Lender
from .models import Borrower
from .models import Object
from .models import User

def index(request):
    
    return render(request, 'app/maketable.html')


def insert(request):
    user1 = User(user_index=1, username='Maria Anders', user_id = 'iamsd',  email = 'afawefwe@gmail.com', addr="경기도 성남시 분당구 불정로 90", pw='12345')
    user2 = User(user_index=2, username='Francisco Chang', user_id = 'soqp', email ='asdasds@gmail.com', addr="경기도 성남시 분당구 이매1동" , pw='235234')
    user3 = User(user_index=3, username='A', user_id = 'dbx', email ='afefewe@gmail.com', addr = "경기도 성남시 분당구 야탑로 59", pw='235234')
    user4 = User(user_index=4, username='B', user_id = 'asdf', email ='ewfefwe@gmail.com',addr ="경기도 성남시 분당구 야탑로161번길 15", pw='123123')
    user5 = User(user_index=5, username='C', user_id = 'oksdf',email ='ap@gmail.com',addr ="경기도 성남시 분당구 야탑3동 283-7", pw='awgweo')
    user6 = User(user_index=6, username='D', user_id = 'wemfo', email ='afase@gmail.com', addr ="경기도 성남시 분당구 야탑3동 장미로 153" , pw='qweqw3')
    user1.save()
    user2.save()
    user3.save()
    user4.save()
    user5.save()
    user6.save()

    l1 = Lender(l_posting_index = 1,	
            lender_index=user2,	
            title='드라이버',	
            category='드라이버',	            
            body = '드라이버 빌려줄게',	
            deposit = 300,	
            pic ='/static/img/object/1.jpg',
            date = '2022-01-22 12:00:00'
            )


    l2 =Lender(l_posting_index = 2,	
            lender_index=user3,	
            title='우산',	
            category='우산',	            
            body = '우산 빌려줄게',	
            deposit = 200,	
            pic ='/static/img/object/2.jpg',
            date = '2022-01-23 12:00:00'
            )

    l3 =Lender(l_posting_index = 3,	
            lender_index=user6,	
            title='커피포트',	
            category='커피포트',	            
            body = '커피포트 필요하면 잠시 빌려줌',	
            deposit = 500,	
            pic ='/static/img/object/3.jpg',
            date = '2022-01-24 12:00:00'
            )

    l4= Lender(l_posting_index = 4,	
            lender_index=user5,	
            title='고기 불판',	
            category='캠핑',	            
            body = '불판 빌려드림',	
            deposit = 1000,	
            pic ='/static/img/object/4.jpg',
            date = '2022-01-25 12:00:00'
            )
            
    l1.save()
    l2.save()
    l3.save()
    l4.save()
    Borrower(b_posting_index = 1,	
            borrower_index=user2,	
            title='테이프',	
            category='테이프',	            
            body = '테이프 좀 빌려줘',	
            date = '2022-01-12 12:00:00'
            ).save()

    Borrower(b_posting_index = 2,	
            borrower_index=user3,	
            title='맥북 충전기',	
            category='전자기기',	            
            body = '맥북 충전기 좀 빌려줘',	
            date = '2022-01-13 12:00:00'
            ).save()


    Borrower(b_posting_index = 3,	
            borrower_index=user5,	
            title='캠핑 도구',	
            category='캠핑',	            
            body = '캠핑 가려는데, 텐트 등 세트 빌립니다~',	
            date = '2022-01-14 12:00:00'
            ).save()

            
    Borrower(b_posting_index = 4,	
            borrower_index=user4,	
            title='방탄 앨범',	
            category='앨범',	            
            body = '방탄 앨범 좀 빌려줘',	
            date = '2022-01-15 12:00:00'
            ).save()

    Object(
        object_index = 1,
        object_name = '드라이버',
        lender_index = 2,
        posting_index = l1,
        deposit = 300
    ).save()
    Object(
        object_index = 2,
        object_name = '우산',
        lender_index = 3,
        posting_index = l2,
        deposit = 200
    ).save()
    Object(
        object_index = 3,
        object_name = '커피포트',
        category = '커피포트',
        lender_index = 6,
        posting_index = l3,
        deposit = 500
    ).save()
    Object(
        object_index = 4,
        object_name = '고기 불판',
        category = '캠핑',
        lender_index = 5,
        posting_index = l4,
        deposit = 1000
    ).save()
    return HttpResponse('ok')
