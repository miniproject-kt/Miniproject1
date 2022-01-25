from django.shortcuts import render
from .models import User, Borrower, Lender

def index(request):
   """
   main 화면
   """
   borrower = Borrower.objects.order_by('-b_posting_index')[:4]
   lender = Lender.objects.order_by('-l_posting_index')[:4]
   context = {
      'borrower': borrower,
      'lender': lender
      }
   return render(request, 'main/main.html', context)