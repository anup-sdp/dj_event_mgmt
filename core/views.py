from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Event, Participant
from .forms import CategoryForm, EventForm, ParticipantForm
from django.utils import timezone
from datetime import date, datetime
from django.db.models import Count, Q
from django.contrib import messages

# Create your views here.
def test_home(request):
    context = {
        "name": "Anup Barua"
    }
    messages.success(request, "sample success message")
    messages.info(request, "sample info message")
    messages.error(request, "sample error message")
    return render(request, "test-home.html", context)


# category views -----------------------------------------------------------------

def category_list(request):    
    categories = Category.objects.annotate(num_events=Count('event'))
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)    
    events = Event.objects.filter(category=category).select_related('category').prefetch_related('participants').all()  #  order by date ?
    return render(request, 'categories/category_detail.html', {'category': category, 'events': events})

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

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.info(request, "category deleted!")
        return redirect('category_list')
    return render(request, 'categories/category_confirm_delete.html', {'category': category})


# event views -----------------------------------------------------------------

def event_list(request):    
    events = Event.objects.select_related('category').prefetch_related('participants').annotate(num_participants=Count('participants')).order_by('date')
    return render(request, 'events/event_list.html', {'events': events, 'heading':'All Events'})


def event_search(request):
    query = request.GET.get('q', '').strip()
    start_date = request.GET.get('start_date', '').strip()
    end_date = request.GET.get('end_date', '').strip()    
    
    events = Event.objects.select_related('category').prefetch_related('participants').annotate(num_participants=Count('participants')).order_by('date')  # all events
    
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
            messages.error(request, "error: Invalid date input")  # Invalid date format
    
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

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "new event created")
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        messages.success(request, "event updated")
        return redirect('event_detail', pk=pk)
    return render(request, 'events/event_form.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.info(request, "event deleted")
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})



# participant views -----------------------------------------------------------------

def participant_list(request):
    # Optionally add search by name or email using GET parameter 'q'
    qs = Participant.objects.annotate(num_events=Count('events'))
    query = request.GET.get('q')
    if query:
        qs = qs.filter(Q(name__icontains=query) | Q(email__icontains=query))        
    participants = qs
    return render(request, 'participants/participant_list.html', {'participants': participants})

def participant_detail(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    events = participant.events.select_related('category').all()
    return render(request, 'participants/participant_detail.html', {'participant': participant, 'events': events})

def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            messages.success(request, "new participant created")
            return redirect('participant_detail', pk=participant.pk)
    else:
        form = ParticipantForm()
    return render(request, 'participants/participant_form.html', {'form': form, 'title': 'Create Participant'})


def participant_update(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, "participant updated")
            return redirect('participant_detail', pk=pk)
    else:
        form = ParticipantForm(instance=participant)
    return render(request, 'participants/participant_form.html', {'form': form, 'title': 'Edit Participant'})


def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        messages.info(request, "participant deletd!")        
        return redirect('participant_list')
    return render(request, 'participants/participant_confirm_delete.html', {'participant': participant})


# Organizer Dashboard view  -----------------------------------------------------------------


def dashboard(request):
    #today = timezone.now().date()
    today = date.today()
    
    total_events = Event.objects.count()
    upcoming_events_count = Event.objects.filter(date__gt=today).count()
    past_events_count = Event.objects.filter(date__lt=today).count()
    # total_participants = Participant.objects.count() # all participants, some may not have participated in events ?
    # total_unique_participants = Participant.objects.filter(events__isnull=False).distinct().count()
    # or, using aggregate:    
    total_unique_participants = Event.objects.aggregate(unique_participants=Count('participants', distinct=True))['unique_participants']  # unpack vaue, aggregate returns a dictionary
                                    
    filter_type = request.GET.get('filter')  # 'total', 'upcoming', 'past', or None

    if filter_type == 'total':
        events_qs = Event.objects.select_related('category').select_related('category').prefetch_related('participants').all()
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