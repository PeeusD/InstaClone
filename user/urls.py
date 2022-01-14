from django.urls import path
from user import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
   
    path('in/<username>/', login_required(views.ProfileView.as_view()), name='profile_view'),
    path('in/<username>/edit/', login_required(views.ProfileEditView.as_view()), name='profile_edit_view'),
    path('profiles/', login_required(views.AllProfilesView.as_view()), name='all_profiles_view'),

 
]
