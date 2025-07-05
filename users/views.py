# users, views.py:
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from core.models import Category, Event
from .forms import UserRegistrationForm, UserUpdateForm
from django.utils import timezone
from datetime import date, datetime
from django.db.models import Count, Q
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required, user_passes_test


def welcome_page(request):
    return render(request, 'welcome-page.html')

def sign_in(request):
    # without using form
    if request.method == 'POST':        
        username = request.POST.get('username')
        password = request.POST.get('password')        
        user = authenticate(request, username=username, password=password)  # None if is_active == False, or wrong username/password         
        if user is not None:
            login(request, user)
            #return redirect('dashboard')
            return redirect('welcome-page')
        else:
            messages.error(request, 'No active user found with these credentials.')
            messages.error(request, 'Check your email and activate account if you have an account, but did not activate already.')
            return redirect('sign-in')    
    #return HttpResponse("<h1>test HttpResponse for login</h1>")
    return render(request, 'participants/sign-in.html')

@login_required
def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign-in')


# user/participant views -----------------------------------------------------------------

def participant_list(request):
    # Search users by username, first_name, last_name, or email
    qs = User.objects.annotate(num_events=Count('rsvp_events'))  # events to rsvp_events ? ----------------------------------------
    query = request.GET.get('q')
    if query:
        qs = qs.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)) 
    users = qs
    return render(request, 'participants/participant_list.html', {'participants': users})

def participant_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    events = user.events.select_related('category').all()
    return render(request, 'participants/participant_detail.html', {'user': user, 'events': events})

def participant_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False # ----- to activate using email.
            user.save()
            messages.success(request, 'A Confirmation mail sent. Please check your email')  # -----
            return redirect('sign-in')
    else:
        form = UserRegistrationForm()
    return render(request, 'participants/participant_register.html', {'form': form, 'title': 'Register'})

def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, f"User account of: { user.username}, has been activated")   
            return redirect('sign-in')
        else:
            return HttpResponse('Invalid Id or token')

    except User.DoesNotExist:
        return HttpResponse('User not found')
    

def participant_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "profile updated")
            return redirect('user_detail', pk=pk)
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'participants/participant_form.html', {'form': form, 'title': 'Edit Profile'})

def participant_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.info(request, "user deleted!")        
        return redirect('participant_list')
    return render(request, 'participants/participant_confirm_delete.html', {'participant': user})


# Organizer Dashboard view  -----------------------------------------------------------------

def dashboard(request):
    today = date.today()
    
    total_events = Event.objects.count()
    upcoming_events_count = Event.objects.filter(date__gt=today).count()
    past_events_count = Event.objects.filter(date__lt=today).count()
    
    # Count unique participants across all events
    total_unique_participants = Event.objects.aggregate(
        unique_participants=Count('participants', distinct=True)
    )['unique_participants']
                                    
    filter_type = request.GET.get('filter')

    if filter_type == 'total':
        events_qs = Event.objects.select_related('category').prefetch_related('participants').all()
        heading = 'All Events'
    elif filter_type == 'upcoming':
        events_qs = Event.objects.filter(date__gt=today).select_related('category').prefetch_related('participants').all()
        heading = 'Upcoming Events'
    elif filter_type == 'past':
        events_qs = Event.objects.filter(date__lt=today).select_related('category').prefetch_related('participants').all()
        heading = 'Past Events'
    else:        
        events_qs = Event.objects.filter(date=today).select_related('category').prefetch_related('participants').all()
        heading = "Today's Events"

    if filter_type == 'past':
        events = events_qs.annotate(num_participants=Count('participants')).order_by('-date', '-time')
    else:
        events = events_qs.annotate(num_participants=Count('participants')).order_by('date', 'time')

    context = {
        'stats': {
            'total_events': total_events,
            'upcoming_events': upcoming_events_count,
            'past_events': past_events_count,
            'total_participants': total_unique_participants,            
        },
        'events': events,
        'heading': heading,
        'filter_type': filter_type,
    }
    return render(request, 'dashboard.html', context)