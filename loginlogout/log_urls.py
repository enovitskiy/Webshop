from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views
from django.contrib import auth

urlpatterns = [
    path(r'', views.login),
    path(r'reg/', views.reg),
    path(r'out/', views.out),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),
    re_path(r'^lo/$', views.dashboard, name='dashboard'),
    re_path(r'^login/$', LoginView.as_view(template_name='account/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(template_name='account/logged_out.html'), name='logout'),
    re_path(r'^password-change/$', PasswordChangeView.as_view(template_name='account/password_change_form.html'), name='password_change'),
    re_path(r'^password-change/done/$', PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),
    re_path(r'^password-reset/$', PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'),
    re_path(r'^password-reset/done/$', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),


]