from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from member.models import User
from argon2 import PasswordHasher # 패스워드 암호화
from argon2.exceptions import VerifyMismatchError


# 회원가입 - 직접 구현
def register(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        pw = request.POST.get('pw')
        confirm_pw = request.POST.get('double_pw')
        username = request.POST.get('username')
        email = request.POST.get('email')

        postid = request.POST.get('postid')
        addr = request.POST.get('addr')

        if User.objects.filter(email = email).exists():
            return redirect('/member/register/')

        # 1차 패스워드와 2차 패스워드가 동일하면 DB 저장
        if pw == confirm_pw:
            m = User(user_id=user_id, pw=PasswordHasher().hash(pw), 
                            username=username, email = email,  addr = addr)
            m.register_date = timezone.now()
            m.save()

            # 이메일 인증 추가
            current_site = get_current_site(request) 
            message = render_to_string('member/act_email.html', {
                'user': m,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(m.pk)),
                'token': account_activation_token.make_token(m),
            })
            mail_title = "쉐어띵즈 계정 활성화 확인 이메일"
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()

            return HttpResponseRedirect('/main/') # 회원가입 성공 후, 메인 페이지로 이동
    
    return render(request, 'member/register.html')

def check_id(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)

    user_id = data['user_id']
    if User.objects.filter(user_id = user_id).exists():
        return HttpResponse("존재")
        
    return JsonResponse(data)




    
# 로그인 - 직접 구현
def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        pw = request.POST.get('pw')

        corr_pw = User.objects.get(user_id=user_id).pw # 암호화 된 pw

        m = User.objects.get(user_id=user_id, pw=corr_pw)

        if m.is_activate == 0:
            return render(request, 'member/login.html')

        request.session['user_id'] = m.user_id
        request.session['username'] = m.username

        return HttpResponseRedirect('/main/')
        
    else:
        return render(request, 'member/login.html')

def valid_login(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)
    
    user_id = data['user_id']
    pw = data['pw']

    # 회원정보 조회 실패 시 예외 발생
    try:
        corr_pw = User.objects.get(user_id=user_id).pw # 암호화 된 pw

        try:
            if PasswordHasher().verify(corr_pw.encode(), pw.encode()): # 패스워드 확인
                return HttpResponse('Success')

        except VerifyMismatchError as e: # 패스워드 틀린 사용자
            return HttpResponse('Error1')

    except User.DoesNotExist as e: # 없는 사용자
        return HttpResponse('Error2')
        
    return JsonResponse(data)


def logout(request):
    del request.session['user_id'] # 개별 삭제
    del request.session['username'] # 개별 삭제
    request.session.flush() # 전체 삭제

    return HttpResponseRedirect('/main/')

    
def find(request):
    return render(request, 'member/finduser.html')

import json
def find_userid(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)

    username = data['username']
    email = data['email']

    try:
        user_id = User.objects.get(username=username, email=email).user_id
        find_info = f"{username}님의 ID는 {user_id}입니다."
        return HttpResponse(find_info)

    except User.DoesNotExist as e:
        return HttpResponse('입력된 정보를 찾을 수 없습니다.')


def reset(request):
    return render(request, 'member/resetpw.html')

import json
def reset_userpw(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)

    user_id = data['user_id']
    email = data['email']
    chg_pw = data['pw']

    try:
        user = User.objects.get(user_id = user_id, email=email)
        user.pw = PasswordHasher().hash(chg_pw)
        user.save()
        return HttpResponse("비밀번호가 변경되었습니다.")

    except User.DoesNotExist as e:
        return HttpResponse('입력된 정보를 찾을 수 없습니다.')

def mypage(request):
    if request.method == 'POST':
        return render(request, 'member/chgMyinfo.html')
    else:
        return render(request, 'member/mypage.html')

def valid_mypage(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)
    
    user_id = data['user_id']
    pw = data['pw']

    if request.session['user_id'] != user_id:
        return HttpResponse('Error2')

    # 회원정보 조회 실패 시 예외 발생
    try:
        corr_pw = User.objects.get(user_id=user_id).pw # 암호화 된 pw

        try:
            if PasswordHasher().verify(corr_pw.encode(), pw.encode()): # 패스워드 확인
                return HttpResponse()

        except VerifyMismatchError as e: # 패스워드 틀린 사용자
            return HttpResponse('Error1')

    except User.DoesNotExist as e: # 없는 사용자
        return HttpResponse('Error2')
        
    return JsonResponse(data)


def chg_info(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/main/')
    else:
        return render(request, 'member/chgMyinfo.html')


def valid_myinfo(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)
    
    user_id = data['user_id']
    curr_pw = data['pw']
    new_pw = data['new_pw']
    username = data['username']
    email = data['email']
    addr = data['addr']

    if request.session['user_id'] != user_id:
        return HttpResponse('Error2')

    # 회원정보 조회 실패 시 예외 발생
    try:
        prev_pw = User.objects.get(user_id=user_id).pw # 암호화 된 pw
        person = User.objects.get(user_id=user_id)

        try:
            if PasswordHasher().verify(prev_pw.encode(), curr_pw.encode()): # 패스워드 확인
                person.pw = PasswordHasher().hash(new_pw)
                person.username = username
                person.email = email
                person.addr = addr
                person.save()
                return HttpResponseRedirect('/main/')

        except VerifyMismatchError as e: # 패스워드 틀린 사용자
            return HttpResponse('Error1')

    except User.DoesNotExist as e: # 없는 사용자
        return HttpResponse('Error2')
        
    return JsonResponse(data)



def del_myinfo(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)
    
    user_id = data['user_id']
    curr_pw = data['pw']


    # 회원정보 조회 실패 시 예외 발생
    try:
        pw = User.objects.get(user_id=user_id).pw # 암호화 된 pw
        person = User.objects.get(user_id=user_id)

        try:
            if PasswordHasher().verify(pw.encode(), curr_pw.encode()): # 패스워드 확인
                person.delete()
                request.session.flush() # 전체 삭제
                #return HttpResponseRedirect('/main/')

        except VerifyMismatchError as e: # 패스워드 틀린 사용자
            return HttpResponse('Error1')

    except User.DoesNotExist as e: # 없는 사용자
        return HttpResponse('Error2')
        
    return JsonResponse(data)



from django.contrib import auth


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token

# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_activate = 1
        user.save()
        return redirect("member:login")

    else:
        return render(request, 'member/login.html', {'error' : '계정 활성화 오류'})