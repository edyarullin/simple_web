from django import forms
from .models import Question, Answer, User
from django.contrib.auth import authenticate


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def set_user(self, user):
        self._user = user
    
    def save(self):
        self.cleaned_data['author'] = self._user
        q = Question(**self.cleaned_data)
        q.save()
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(required=False, widget=forms.HiddenInput, label='')

    def set_fields(self, user, q):
        self._user = user
        self._question = q
    
    def save(self):
        self.cleaned_data['author'] = self._user
        self.cleaned_data['question'] = self._question
        ans = Answer(**self.cleaned_data)
        ans.save()
        return ans


class SignupForm(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def save(self):
        return User.objects.create_user(**self.cleaned_data)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean(self):
        user = authenticate(**self.cleaned_data)
        if user is None:
            raise forms.ValidationError('Введен неверный логин и/или пароль', code=10)
        self._user = user

    def get_user(self):
        return self._user
