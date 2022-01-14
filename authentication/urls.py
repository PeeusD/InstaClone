from django.urls import path, reverse_lazy
from authentication import views

from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView, PasswordChangeDoneView
urlpatterns = [
    path('', views.LogInView.as_view(), name='log_in'),
    path('signup/', views.SignUpView.as_view(), name='sign_up'),
    path('logout/', views.LogOutView.as_view(), name='log_out'),

  
    path('password/reset/', PasswordResetView.as_view( template_name = 'authentication/password_reset.html' ), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(  template_name = 'authentication/password_reset_confirm.html' ), name='password_reset_confirm'),
    path('password/reset/done/', PasswordResetDoneView.as_view(  template_name = 'authentication/password_reset_done.html' ), name='password_reset_done'),
    path('password/reset/complete/', PasswordResetCompleteView.as_view( template_name = 'authentication/password_reset_complete.html' ), name='password_reset_complete'),
    
    path('password/change/', PasswordChangeView.as_view(template_name = 'authentication/password_change.html', success_url=reverse_lazy('password_change_done_view')), name='password_change_view'),
    path('password/change/done/', PasswordChangeDoneView.as_view(template_name = 'authentication/password_change_done.html'), name='password_change_done_view'),

 
]

  # path('password/reset/', views.PRView.as_view(), name='password_reset'),
    # path('password/reset/confirm/<uidb64>/<token>',views.PRConfirm.as_view(), name='password_reset_confirm'),
    # path('password/reset/done/', views.PRDone.as_view(), name='password_reset_done'),
    # path('password/reset/complete/', views.PRComplete.as_view(), name='password_reset_complete'),
    