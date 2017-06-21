from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from posts.models import Profile
from django.core.files.images import get_image_dimensions

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Full name")

    class Meta:
        model = User
        fields = ("username", "fullname", "email", )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        first_name, last_name = self.cleaned_data["fullname"].split()
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)

class UpdateUser(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required= True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    #def clean_email(self):
        #username = self.cleaned_data.get('username')
        #email = self.cleaned_data.get('email')

        #if email and User.objects.filter(email=email).exclude(username=username).count():
            #raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        #return email

class UpdateBio(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Profile
        fields = ('bio',)

    def clean_bio(self):
        cleaned_bio = self.cleaned_data.get('bio')
        return cleaned_bio

class UpdateAvatar(forms.ModelForm):
    avatar = forms.CharField(widget=forms.Textarea, required=True)
    
    class Meta:
        model = Profile
        fields = ('avatar',)

    def clean_avatar(self):
        cleaned_avatar = self.cleaned_data.get('avatar')
        return cleaned_avatar