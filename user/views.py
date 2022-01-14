from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import get_user_model
from user.forms import UserEditForm
from django.contrib import messages
from django.db.models import Q
from core.models import Follow
# Create your views here.

User = get_user_model()

class ProfileView(View):

#Showing all peoples' profile details...
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')

        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('<h1>404 :(</h1> <br> <h3>File not found!</h3>')

        if username == request.user.username:
            return render(request, 'user/authenticated_profile.html', context={'user': user})
        else:
            #follow/unfollow button with conditional statement switching...
            try:
                Follow.objects.get(user=request.user, followed=user)
                is_follows_this_user = True
            except:
                is_follows_this_user= False
            #getting all the follower people of specific user
            
            return render(request, 'user/anonymous_profile.html', context={'user': user, 'is_follows_this_user':is_follows_this_user})    
       
class ProfileEditView(View):

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username') #gettting user sessions from request obj

        if username != request.user.username:
            return HttpResponse('<h1>404 :(</h1> <br> <h3>File not found!</h3>')

        form = UserEditForm(instance= request.user)   # populating the user instance in form;  request.user is user obj (stores current user session)
        return render(request, 'user/profile_edit.html', context={'form':form})

    def post(self, request, *args, **kwargs):
        form = UserEditForm(request.POST, request.FILES, instance=request.user)   
        # request.POST stores all form values in query dict, reequest.FILES stores all files, request.user is user obj (stores user session)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your personal details has been successfully saved.')
            return redirect('profile_edit_view', request.user.username)
        else:
            return render(request, 'user/profile_edit.html', context={'form':form})

class AllProfilesView(View):
    
    def get(self, request, *args, **kwargs):
        search_res = request.GET.get('search_query')
        if search_res:
            #exclude removes the params pssed into it & filter() ->filters the results a/c to given values in searchbox
            all_profiles = User.objects.all().filter(Q(full_name__contains=search_res) | Q (full_name__contains=search_res)
            ).exclude(username=request.user.username) 
        else:
            all_profiles = User.objects.none()   #passing empty values validation
        return render(request, 'user/all_profiles.html', context={'all_profiles':all_profiles})