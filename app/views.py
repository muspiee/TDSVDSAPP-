from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from Accounts.models import *
from django.utils import timezone
from datetime import timedelta
from django.utils.dateparse import parse_datetime


def contact(request):
    sponser = sponsers.objects.all()
    return render(request, 'contact.html', {'sponsers': sponser})


def whattodo(request):
    sponser = sponsers.objects.all()
    return render(request, 'what.html', {'sponsers': sponser})


def users(request):
    user = Pot.objects.all()
    sponser = sponsers.objects.all()
    return render(request, 'users.html', {'sponsers': sponser, 'user': user})


def about(request):
    sponser = sponsers.objects.all()
    return render(request, 'abount us.html', {'sponsers': sponser})


def mission(request):
    sponser = sponsers.objects.all()
    return render(request, 'mission.html', {'sponsers': sponser})


def use(request):
    sponser = sponsers.objects.all()
    return render(request, 'use.html', {'sponsers': sponser})


def how(request):
    sponser = sponsers.objects.all()
    return render(request, 'how.html', {'sponsers': sponser})


def home(request):
    current_time = timezone.now()

    # Check if the timer has started.
    if 'timer_start' in request.session:
        # Retrieve the start time from session and parse it back to datetime
        start_time = parse_datetime(request.session['timer_start'])

        # Calculate elapsed time since timer start.
        if current_time - start_time > timedelta(minutes=3):
            # Timer expired, check if the user is logged in and paid.
            if request.user.is_authenticated and request.user.is_paid:
                # Set is_paid to False because the timer expired.
                request.user.is_paid = False
                request.user.save()

            # Regardless of user status, reset the timer and the timer_expired flag.
            request.session['timer_start'] = current_time.isoformat()  # Reset timer
            request.session['timer_expired'] = True  # Indicate that the timer has expired.
        else:
            # If the timer has not expired, update session to ensure it's still active.
            request.session.modified = True
    else:
        # Initialize the timer if it's not already set and store it as a string in ISO format.
        request.session['timer_start'] = current_time.isoformat()
        request.session['timer_expired'] = False  # Start with the timer not expired.

    # Your regular view logic here.
    sponser = sponsers.objects.all()
    return render(request, 'index.html', {'sponsers': sponser})


@login_required
def deactivate_user(request):
    user = request.user
    if user.is_authenticated:
        user.is_paid = False
        user.save()
        return JsonResponse({'status': 'success', 'message': 'User deactivated successfully.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'User is not authenticated.'})


@csrf_exempt
def get_spelling_suggestions(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term', '')
        suggestions = list(VDSTDS.objects.filter(name__icontains=search_term).values_list('name', flat=True)[:5])
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'error': 'Invalid request'})




@login_required
def search(request):
    show_search_form = True
    search_results = None
    if request.method == 'POST':
        if 'search_start_time' not in request.session:
            request.session['search_start_time'] = timezone.now().isoformat()
        search_start_time = timezone.datetime.fromisoformat(request.session['search_start_time'])
        time_elapsed = timezone.now() - search_start_time
        if time_elapsed > timedelta(minutes=3):
            print("Timer Expired.")
            show_search_form = False
            request.session['search_start_time'] = timezone.now().isoformat()
        if show_search_form:
            if request.user.is_paid:
                search_term = request.POST.get('search', '')
                search_results = VDSTDS.objects.filter(name__iexact=search_term)
            else:
                return redirect('renew_account')
    return render(request, 'search.html', {
        'search_results': search_results,
        'show_search_form': show_search_form
    })


@login_required
def renew_account(request):
    return render(request, 'renew.html')


def activation_view(request):
    return render(request, 'active.html')
