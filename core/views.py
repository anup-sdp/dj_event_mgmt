# Participant, participants to User

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Category, Event
from .forms import CategoryForm, EventForm
from django.utils import timezone
from datetime import date, datetime
from django.db.models import Count, Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import Http404

# Create your views here.

def no_permission(request, exception=None): # handle direct access and 403 errors
    return render(request, 'no_permission.html')


def is_in_groups(user):
    return user.groups.filter(name__in=['Admin', 'Organizer', 'Participant']).exists()


def test_home(request):
    context = {
        "name": "Anup Barua"
    }
    messages.success(request, "sample success message")
    messages.info(request, "sample info message")
    messages.error(request, "sample error message")
    return render(request, "test-home.html", context)


# category views -----------------------------------------------------------------


@user_passes_test(is_in_groups, login_url='no-permission')
def category_list(request):    
    categories = Category.objects.annotate(num_events=Count('events'))
    return render(request, 'categories/category_list.html', {'categories': categories})


@user_passes_test(is_in_groups, login_url='no-permission')
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)    
    events = Event.objects.filter(category=category).select_related('category').prefetch_related('participants').all()
    return render(request, 'categories/category_detail.html', {'category': category, 'events': events})


@permission_required("core.add_category", login_url='no-permission')
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "new category created")
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form, 'title': 'Create Category'})

@permission_required("core.change_category", login_url='no-permission')
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "category updated")
            return redirect('category_detail', pk=pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form, 'title': 'Edit Category'})

@permission_required("core.delete_category", login_url='no-permission')
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.info(request, "category deleted!")
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})


# event views -----------------------------------------------------------------

@user_passes_test(is_in_groups, login_url='no-permission')
def event_list(request):    
    events = Event.objects.select_related('category').prefetch_related('participants').annotate(num_participants=Count('participants')).order_by('date')
    return render(request, 'events/event_list.html', {'events': events, 'heading':'All Events'})

@user_passes_test(is_in_groups, login_url='no-permission')
def event_add_rsvp(request, event_id):    
    event = get_object_or_404(Event, id=event_id)    
    if event.participants.filter(id=request.user.id ).exists():
        messages.info(request, "You are already registered for this event.")
    else:        
        event.participants.add(request.user.id)
        messages.success(request, "Successfully registered for the event!")    
    
    redirect_url = request.META.get('HTTP_REFERER', '/')
    return redirect(redirect_url) # redirect back to the previous page   


@user_passes_test(is_in_groups, login_url='no-permission')
def event_remove_rsvp(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if event.participants.filter(id=request.user.id).exists():
        event.participants.remove(request.user)
        messages.success(request, "Successfully unregistered from the event")
    else:
        messages.info(request, "You're not registered for this event")
    
    return redirect(request.META.get('HTTP_REFERER', '/'))


def event_search(request):
    query = request.GET.get('q', '').strip()
    start_date = request.GET.get('start_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()    
    
    events = Event.objects.select_related('category').prefetch_related('participants').annotate(num_participants=Count('participants')).order_by('date')
    
    filters_applied = []
   
    if query:
        events = events.filter(Q(name__icontains=query) | Q(category__name__icontains=query))
        filters_applied.append(f'matching "{query}"')    

    if start_date:
        try:
            start_date_parsed = datetime.strptime(start_date, '%Y-%m-%d').date()
            events = events.filter(date__gte=start_date_parsed)
            filters_applied.append(f'from {start_date_parsed.strftime("%B %d, %Y")}')
        except ValueError:
            messages.error(request, "error: Invalid date input")
    
    if end_date:
        try:
            end_date_parsed = datetime.strptime(end_date, '%Y-%m-%d').date()
            events = events.filter(date__lte=end_date_parsed)
            filters_applied.append(f'until {end_date_parsed.strftime("%B %d, %Y")}')
        except ValueError:
            messages.error(request, "error: Invalid date input")
    
    if filters_applied:
        heading = f'Events {" and ".join(filters_applied)}'
        results_count = events.count()
    else:
        heading = 'All Events'
        results_count = None
    
    context = {
        'events': events,
        'heading': heading,
        'query': query,
        'start_date': start_date,
        'end_date': end_date,
        'results_count': results_count,
        'has_filters': bool(query or start_date or end_date)
    }    
    return render(request, 'events/event_list.html', context)

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

@permission_required("core.add_event", login_url='no-permission')
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "new event created")
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})


@permission_required("core.change_event", login_url='no-permission')
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if form.is_valid():
        form.save()
        messages.success(request, "event updated")
        return redirect('event_detail', pk=pk)
    return render(request, 'events/event_form.html', {'form': form})


@permission_required("core.delete_event", login_url='no-permission')
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.info(request, "event deleted")
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})


