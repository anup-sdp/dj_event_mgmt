# users, urls.py:
from django.urls import path
from users import views 


urlpatterns = [
	path('participants/', views.participant_list, name='participant_list'),  # http://127.0.0.1:8000/participants/
    path('participants/register/', views.participant_register, name='participant_create'),
	path('activate/<int:user_id>/<str:token>/', views.activate_user),  # email activation
    path('participants/<int:pk>/', views.participant_detail, name='participant_detail'),
    path('participants/<int:pk>/update/', views.participant_update, name='participant_update'),
	path('participants/<int:user_id>/update-role/', views.update_participant_role, name='update_participant_role'),
    path('participants/<int:pk>/delete/', views.participant_delete, name='participant_delete'),
	path('sign-in/', views.sign_in, name='sign-in'), 
	path('sign-out/', views.sign_out, name='sign-out'),
	path('users-welcome-page/', views.welcome_page, name='users-welcome-page'),  # http://127.0.0.1:8000/users/welcome-page/
	path('organizer-dashboard/', views.organizer_dashboard, name='organizer-dashboard'), # organizer dashboard  # http://127.0.0.1:8000/users/organizer-dashboard/
	path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
	path('participant-dashboard/', views.participant_dashboard, name='participant-dashboard'),
]
# users/