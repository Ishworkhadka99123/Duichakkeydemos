from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from registration import urls as core_urls #Password App Urls
from shop import urls as shop_urls
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include(core_urls)), #Password App Urls
    path('', include(shop_urls)), #Password App Urls
    # path('accounts/', include('allauth.urls')),
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # Main Page 
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    # Change Password
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html', success_url = '/'), name='change_password'),
    # Forget Password
    path('password-reset/',auth_views.PasswordResetView.as_view(
             template_name='registration/password-reset/password_reset.html',
             subject_template_name='registration/password-reset/password_reset_subject.txt',
             email_template_name='registration/password-reset/password_reset_email.html',
             success_url='/password-reset/done/'
         ),
         name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password-reset/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password-reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password-reset/password_reset_complete.html'), name='password_reset_complete'),
]

# urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)