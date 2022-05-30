from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/', views.UserListView.as_view(), name='userlist'),
    path('user/<int:pk>/', views.UserView.as_view(), name='user'),
    path('announcements/', views.AnnouncementListView.as_view(), name='announcements'),
    path('announcement/add/', views.AnnouncementCreateView.as_view(), name='announcement-add'),
    path('announcement/<int:pk>/', views.AnnouncementUpdateView.as_view(), name='announcement-update'),
    path('announcement/<int:pk>/delete/', views.AnnouncementDeleteView.as_view(), name='announcement-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)