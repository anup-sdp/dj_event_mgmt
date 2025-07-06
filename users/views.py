# users, views.py:
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from core.models import Category, Event
from .forms import UserRegistrationForm, UserUpdateForm, CreateGroupForm
from django.utils import timezone
from datetime import date, datetime
from django.db.models import Count, Q
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import Group

def welcome_page(request):
    return render(request, 'welcome-page.html')

def is_admin(user):    
    return user.groups.filter(name='Admin').exists()  # also add if superuser

def is_organizer(user):    
    return user.groups.filter(name='Organizer').exists()

def is_participant(user):    
    return user.groups.filter(name='Participant').exists()

def sign_in(request):
    # without using form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')        
        user = authenticate(request, username=username, password=password)  # None if is_active == False, or wrong username/password         
        if user is not None:
            login(request, user)
            #return redirect('dashboard')
            if user.groups.filter(name='Admin').exists():
                return redirect('admin-dashboard')
            elif user.groups.filter(name='Organizer').exists():
                return redirect('organizer-dashboard')
            elif user.groups.filter(name='Participant').exists():
                return redirect('participant-dashboard')
            else:
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
    qs = User.objects.annotate(num_events=Count('rsvp_events')).prefetch_related('groups')  # changed events to rsvp_events
    # Search users by username, first_name, last_name, or email
    query = request.GET.get('q')
    if query:
        qs = qs.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)) 
    users = qs
    return render(request, 'participants/participant_list.html', {'participants': users})


def participant_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    events = user.rsvp_events.select_related('category').all()
    #events = user.events.select_related('rsvp_events').all()
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
    

    
@user_passes_test(is_admin, login_url='no-permission')
def participant_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        #form = UserUpdateForm(request.POST, instance=user) # the form dont have email field so add it.
        post_data = request.POST.copy()        
        post_data['email'] = user.email
        form = UserUpdateForm(post_data, instance=user)        
        if form.is_valid():
            form.save()
            print("profile updated")
            messages.success(request, "profile updated")            
            return redirect('participant_list')
        else:
            print(form.errors)   # debug
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'participants/participant_update_form.html', {'form': form, 'title': 'Edit Profile'})

@user_passes_test(is_admin, login_url='no-permission')
def update_participant_role(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        # Process form submission here
        new_role_id = request.POST.get('role')
        new_role = get_object_or_404(Group, id=new_role_id)
        
        # Clear existing groups and add new role
        user.groups.clear()
        user.groups.add(new_role)
        messages.success(request, f"Role updated for {user.username}")  
        return redirect('participant_list')
    
    # GET request - show role selection form
    roles = Group.objects.filter(name__in=["Admin", "Organizer", "Participant"])
    current_role = user.groups.first()
    
    return render(request, 'participants/edit_role.html', {
        'user': user,
        'roles': roles,
        'current_role': current_role
    })

@user_passes_test(is_admin, login_url='no-permission')
def participant_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        messages.info(request, "user account deleted!")        
        return redirect('participant_list')
    return render(request, 'participants/participant_confirm_delete.html', {'participant': user})

# groups ------------------------------------------
@user_passes_test(is_admin, login_url='no-permission')
def create_group(request):
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)

        if form.is_valid():
            group = form.save()
            messages.success(request, f"Group { group.name} has been created successfully")                            
            return redirect('group-list')

    return render(request, 'create_group.html', {'form': form})


@user_passes_test(is_admin, login_url='no-permission')
def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()  # resolve 1+n problem
    return render(request, 'group_list.html', {'groups': groups})

@user_passes_test(is_admin, login_url='no-permission')
def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        group.delete()
        messages.success(request, f'The group "{group.name}" has been deleted successfully.')
        return redirect('group-list')    
    return redirect('group-list')


# Dashboard views -----------------------------------------------------------------
@user_passes_test(is_admin, login_url='no-permission')
def admin_dashboard(request):    
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
        
    rsvp_events = request.user.rsvp_events.all().order_by('date') # self events
    
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
        'rsvp_events': rsvp_events
    }
    return render(request, 'admin_dashboard.html', context)

@user_passes_test(is_participant, login_url='no-permission')
def participant_dashboard(request):
    rsvp_events = request.user.rsvp_events.all().order_by('date')    
    context = {'events': rsvp_events}
    return render(request, 'participant_dashboard.html', context)
    

@user_passes_test(is_organizer, login_url='no-permission')
def organizer_dashboard(request):
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
        
    rsvp_events = request.user.rsvp_events.all().order_by('date') # self events
    
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
        'rsvp_events': rsvp_events
    }
    return render(request, 'organizer_dashboard.html', context)