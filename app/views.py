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
    User(user_index=1, username='Maria Anders', user_id = 'iamsd',  email = 'afawefwe@gmail.com', pw='12345').save()
    User(user_index=2, username='Francisco Chang', user_id = 'soqp', email ='asdasds@gmail.com', pw='235234').save()
    User(user_index=3, username='A', user_id = 'dbx', email ='afefewe@gmail.com', pw='235234').save()
    User(user_index=4, username='B', user_id = 'asdf', email ='ewfefwe@gmail.com', pw='123123').save()
    User(user_index=5, username='C', user_id = 'oksdf',email ='ap@gmail.com', pw='awgweo').save()
    User(user_index=6, username='D', user_id = 'wemfo', email ='afase@gmail.com', pw='qweqw3').save()


    Lender(l_posting_index = 1,	
            lender_index=2,	
            title='드라이버',	
            category='드라이버',	            
            body = '드라이버 빌려줄게',	
            rentalfee = 300,	
            longitude = 32.1,	
            latitude = 123.6,
            object_num = 1,	
            pic ='/static/img/object/1.jpg',
            date = '2022-01-22 12:00:00'
            ).save()


    Lender(l_posting_index = 2,	
            lender_index=3,	
            title='우산',	
            category='우산',	            

            body = '우산 빌려줄게',	
            rentalfee = 200,	
            longitude = 32.134,	
            latitude = 122.612,
            object_num = 2,	
            pic ='/static/img/object/2.jpg',
            date = '2022-01-23 12:00:00'
            ).save()

    Lender(l_posting_index = 3,	
            lender_index=6,	
            title='커피포트',	
            category='커피포트',	            

            body = '커피포트 필요하면 잠시 빌려줌',	
            rentalfee = 500,	
            longitude = 31.123,	
            latitude = 129.612,
            object_num = 3,	
            pic ='/static/img/object/3.jpg',
            date = '2022-01-24 12:00:00'
            ).save()

    Lender(l_posting_index = 4,	
            lender_index=5,	
            title='고기 불판',	
            category='캠핑',	            

            body = '불판 빌려드림',	
            rentalfee = 1000,	
            longitude = 21.134,	
            latitude = 172.612,
            object_num = 4,	
            pic ='/static/img/object/4.jpg',
            date = '2022-01-25 12:00:00'
            ).save()



    Borrower(b_posting_index = 1,	
            borrower_index=2,	
            title='테이프',	
            category='테이프',	            
            body = '테이프 좀 빌려줘',	
            longitude = 11.1,	
            latitude = 120.6,
            date = '2022-01-12 12:00:00'
            ).save()

    Borrower(b_posting_index = 2,	
            borrower_index=3,	
            title='맥북 충전기',	
            category='전자기기',	            
            body = '맥북 충전기 좀 빌려줘',	
            longitude = 12.8,	
            latitude = 129.6,
            date = '2022-01-13 12:00:00'
            ).save()


    Borrower(b_posting_index = 3,	
            borrower_index=5,	
            title='캠핑 도구',	
            category='캠핑',	            
            body = '캠핑 가려는데, 텐트 등 세트 빌립니다~',	
            longitude = 12.43,	
            latitude = 123.642,
            date = '2022-01-14 12:00:00'
            ).save()

            
    Borrower(b_posting_index = 4,	
            borrower_index=4,	
            title='방탄 앨범',	
            category='앨범',	            
            body = '방탄 앨범 좀 빌려줘',	
            longitude = 43.1,	
            latitude = 122.6,
            date = '2022-01-15 12:00:00'
            ).save()

    Object(
        object_index = 1,
        object_name = '드라이버',
        borrower_index = 0,
        lender_index = 2,
        posting_index = 1,
        rental_fee = 300,
        longitude = 32.134,
        latitude = 122.612
    ).save()
    Object(
        object_index = 2,
        object_name = '우산',
        borrower_index = 1,
        lender_index = 3,
        posting_index = 2,
        rental_fee = 200,
        longitude = 32.1,
        latitude = 123.6
    ).save()
    Object(
        object_index = 3,
        object_name = '커피포트',
        category = '커피포트',
        borrower_index = 0,
        lender_index = 6,
        posting_index = 3,
        rental_fee = 500,
        longitude = 31.123,	
        latitude = 129.612
    ).save()
    Object(
        object_index = 4,
        object_name = '고기 불판',
        category = '캠핑',
        borrower_index = 6,
        lender_index = 5,
        posting_index = 4,
        rental_fee = 1000,
        longitude = 21.134,	
        latitude = 172.612
    ).save()
    return HttpResponse('ok')
