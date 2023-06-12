from post.models import Comment
from post.models import Post
from django import forms 
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
class UserRegistrationForm(forms.ModelForm):
    password1=forms.CharField(label=' пароль',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтарите пароль',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']