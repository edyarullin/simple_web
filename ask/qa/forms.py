from django import forms
from .models import Question, Answer, User

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        self._user = User.objects.get(id=1)
        super(AskForm, self).__init__(*args, **kwargs)

    def save(self):
        self.cleaned_data['author'] = self._user
        q = Question(**self.cleaned_data)
        q.save()
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

    def __init__(self, question, *args, **kwargs):
        self._user = User.objects.get(id=1)
        self._question = question
        super(AnswerForm, self).__init__(*args, **kwargs)
    
    def save(self):
        self.cleaned_data['author'] = self._user
        self.cleaned_data['question'] = self._question
        ans = Answer(**self.cleaned_data)
        ans.save()
        return ans
