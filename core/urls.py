# core, urls.py:
from django.urls import path
from . import views 
from users.views import welcome_page

urlpatterns = [    
	path('test-home/', views.test_home, name='test-home'),  # http://127.0.0.1:8000/test-home/	
	path('', welcome_page, name='welcome-page'),  # http://127.0.0.1:8000/

	path('event-list/', views.event_list, name='event_list'),  # list of all events  # http://127.0.0.1:8000/event-list/
	path('event_search/', views.event_search, name='event_search'),
	path('create/', views.event_create, name='event_create'),    
    path('<int:pk>/', views.event_detail, name='event_detail'),  # single event  event_add_rsvp
    path('<int:pk>/update/', views.event_update, name='event_update'),    
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),
	path('<int:event_id>/add_rsvp/', views.event_add_rsvp, name='event_add_rsvp'), # ------------ 
	path('<int:event_id>/remove_rsvp/', views.event_remove_rsvp, name='event_remove_rsvp'),

	path('categories/', views.category_list, name='category_list'),  # http://127.0.0.1:8000/categories/
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),	
]
