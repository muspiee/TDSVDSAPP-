from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Users
import random
import re

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not phone:
            messages.error(request, 'Please provide Your Mobile Number.')
            return render(request, 'signup.html')
        if not phone.isdigit() or len(phone) != 11:
            messages.error(request, 'Please enter a valid phone number with exactly 11 digits.')
            return render(request, 'signup.html')
        if not name:
            messages.error(request, 'Please provide Your Name.')
            return render(request, 'signup.html')
        if not email:
            messages.error(request, 'Please provide an Email Address.')
            return render(request, 'signup.html')
        if not re.fullmatch(email_regex, email):
            messages.error(request, 'Invalid email format.')
            return render(request, 'signup.html')
        if not password:
            messages.error(request, 'Please provide a Password.')
            return render(request, 'signup.html')
        if Users.objects.filter(name=name).exists():
            messages.error(request, 'Username already used')
        elif Users.objects.filter(email=email).exists():
            messages.error(request, 'Email already used')
        elif Users.objects.filter(username=phone).exists():
            messages.error(request, 'Phone number already used')
        else:
            otp = random.randint(100000, 999999)
            user = Users.objects.create(name=name, username=phone, email=email, otp=otp)
            user.set_password(password)
            user.save()
            subject = 'Account Verification OTP'
            message = f'Hi {name}, Thanks for registering to TDSVDS Live Dictionary, here is your OTP: {otp}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Check your email/spam folder for OTP')
            return redirect('otp')
    return render(request, 'signup.html')

def otp_verify(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        if otp:
            user = Users.objects.filter(otp=otp).first()
            if user:
                user.is_verified = True
                user.save()
                messages.success(request, "Account verified. Please log in.")
                return redirect('login')
            else:
                messages.error(request, 'No user found.')
        else:
            messages.error(request, 'OTP is required.')
    return render(request, 'otp.html')

def user_logout(request):
    logout(request)
    messages.error(request, "User logged out!")
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(request, username=phone, password=password)
        if user:
            if user.is_verified:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('home')
            else:
                messages.error(request, "Account not verified.")
                return redirect('otp')
        else:
            messages.error(request, 'Invalid credentials or user does not exist.')
    return render(request, 'login.html')