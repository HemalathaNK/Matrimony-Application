from django.urls import path
from app1 import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.login_fun,name='login'),
    path('signup/',views.signup_fun,name='signup'),

    path('brides_profiles/', views.brides_profiles, name='brides_profiles'),
    path('brides_profiles/b_details/<int:id>/', views.bride_details, name='bride_details'),

    path('grooms_profiles/', views.grooms_profiles, name='grooms_profiles'),
    path('grooms_profiles/g_details/<int:id>/', views.groom_details, name='groom_details'),

    path('profile/',views.profile_fun,name='profile'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),

    path('home/', views.home_page, name='home'),
    path('home/details/<int:id>/', views.see_details, name='see_details'),

    path('search_profiles/', views.search_profiles, name='search_profiles'),

    path('logout/',views.logout_fun,name='logout'),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete')
]