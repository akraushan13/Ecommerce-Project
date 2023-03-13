from django.urls import path
from account import views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='login'),
    path('logout/',views.handlelogout,name='logout'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    path('request_reset_email/',views.RequestResetEmailView.as_view(),name='request_reset_email'),
    path('set_new_password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set_new_password'),
]
