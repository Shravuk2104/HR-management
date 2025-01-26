from django.conf.urls.static import static
from hr_Management import settings
from hrm_app import views
from django.urls import path

urlpatterns = [
    path('dashboard',views.dashboard),
    path('department',views.department),
    path('add/', views.add_department, name='add_department'),
    path('update/<int:dept_id>/', views.update_department, name='update_department'),
    path('delete/<int:dept_id>/', views.delete_department, name='delete_department'),
    path('upcoming_events/', views.upcoming_events, name='upcoming_events'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)