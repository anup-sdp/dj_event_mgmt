# users, urls.py:
from django.urls import path
from users import views 
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
	#path('sign-in/', views.sign_in, name='sign-in'), 
	path('sign-in/', views.SignInView.as_view(), name='sign-in'), # new cbv
	path('sign-out/', views.sign_out, name='sign-out'),
	path('users-welcome-page/', views.welcome_page, name='users-welcome-page'),  # http://127.0.0.1:8000/users/welcome-page/
	path('dashboard/', views.dashboard, name='dashboard'),
	#path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
	path('admin-dashboard/', views.AdminDashboardView.as_view(), name='admin-dashboard'), # new cbv
	path('organizer-dashboard/', views.organizer_dashboard, name='organizer-dashboard'), # organizer dashboard  # http://127.0.0.1:8000/users/organizer-dashboard/	
	path('participant-dashboard/', views.participant_dashboard, name='participant-dashboard'),
	#path('participants/', views.participant_list, name='participant_list'),  # http://127.0.0.1:8000/users/participants/
	path('participants/', views.ParticipantListView.as_view(), name='participant_list'), # new cbv
    path('participants/register/', views.participant_register, name='participant_create'),
	path('activate/<int:user_id>/<str:token>/', views.activate_user),  # email activation
    path('participants/<int:pk>/', views.participant_detail, name='participant_detail'),
    path('participants/<int:pk>/update/', views.participant_update, name='participant_update'),
	path('participants/<int:user_id>/update-role/', views.update_participant_role, name='update_participant_role'),
    path('participants/<int:pk>/delete/', views.participant_delete, name='participant_delete'),		
	path('admin/create-group/', views.create_group, name='create-group'),
    path('admin/group-list/', views.group_list, name='group-list'),
	path('groups/delete/<int:group_id>/', views.delete_group, name='delete_group'),
	path('profile/', views.ProfileView.as_view(), name='profile'), # cbv
	path('edit-profile/', views.EditProfileView.as_view(), name='edit_profile'), # cbv
	path('password-change/', views.ChangePassword.as_view(), name='password_change'),  # cbv
	path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
	path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),  # cbv
    path('password-reset/confirm/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # cbv
]
# converted old fbv to cbv: SignInView, ParticipantListView, AdminDashboardView

# users/