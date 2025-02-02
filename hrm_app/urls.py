from hrm_app import views
from django.urls import path
from hr_Management import settings
from django.conf.urls.static import static
from hrm_app.views import user_login, user_logout, CustomPasswordResetView, PasswordResetConfirmView, reset_password, verify_otp, request_otp
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard', views.dashboard),
    path('department', views.department),
    path('add/', views.add_department, name='add_department'),
    path('update/<int:dept_id>/', views.update_department, name='update_department'),
    path('delete/<int:dept_id>/', views.delete_department, name='delete_department'),
    path('upcoming_events/', views.upcoming_events, name='upcoming_events'),
     path('roles/', views.roless, name='roless'),  # URL for roles view
    path('roles/add/', views.add_role, name='add_role'), 
    path('roles/update/<int:role_id>/', views.update_role, name='update_role'),
    path('roles/delete/<int:role_id>/', views.delete_role, name='delete_role'),
    path('employee', views.employee),
     path('employee/add/', views.add_employee, name='add_employee'), 
    path('employee/update/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('employee/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # Password reset request (enter email)
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),

    # Password reset done (confirmation message after email sent)
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    # Password reset confirm (user enters new password)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    # Password reset complete (after password reset success)
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # Custom password reset page (after login, mandatory reset)
    path('reset_password/', reset_password, name='reset_password'),

    path('verify-otp/', verify_otp, name='verify_otp'),
    path('forgot-password/', request_otp, name='forgot_password'),
    path('request_otp/', request_otp, name='request_otp'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
