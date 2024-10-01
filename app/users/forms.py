from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'bio', 'location', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 20, 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'type': "file", 'id': "id_profile_picture", 'name': "profile_picture", 'class': "form-control"})
        }

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            if not form.cleaned_data['profile_picture']:
                form.instance.profile_picture = 'default/profile_photo.jpg'
            form.save()
            return redirect('users:profile', user_id = request.user.id)  # Redirect to the appropriate page after saving
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form, 'user': request.user})