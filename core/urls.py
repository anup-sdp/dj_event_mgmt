from django.urls import path
from . import views 

urlpatterns = [    
	path('test-home/', views.test_home, name='test-home'),  # http://127.0.0.1:8000/test-home/	

	path('', views.event_list, name='event_list'),  # list of all events  # http://127.0.0.1:8000/
	path('event_search/', views.event_search, name='event_search'),
	path('create/', views.event_create, name='event_create'),    
    path('<int:pk>/', views.event_detail, name='event_detail'),  # single event  
    path('<int:pk>/update/', views.event_update, name='event_update'),    
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),

	path('categories/', views.category_list, name='category_list'),  # http://127.0.0.1:8000/categories/
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

	path('participants/', views.participant_list, name='participant_list'),  # http://127.0.0.1:8000/participants/
    path('participants/register/', views.participant_register, name='participant_create'),
    path('participants/<int:pk>/', views.participant_detail, name='participant_detail'),
    path('participants/<int:pk>/update/', views.participant_update, name='participant_update'),
    path('participants/<int:pk>/delete/', views.participant_delete, name='participant_delete'),

	path('dashboard/', views.dashboard, name='dashboard'), # organizer dashboard  # http://127.0.0.1:8000/dashboard/
]

