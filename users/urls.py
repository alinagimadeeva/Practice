from django.urls import path
from . import services, views

app_name = 'users'

urlpatterns = [
    path('staff/panel/', views.StaffPanelView.as_view(), name='staff_panel'),
    path(
        'staff/panel/handle/<int:request_id>/<str:action>/',
        services.handle_teacher_request,
        name='handle_teacher_request'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path(
        'password_change/',
        views.PasswordChangeView.as_view(),
        name='password_change'),
    path('profile/', views.UserProfileView.as_view(), name='profile')


]
