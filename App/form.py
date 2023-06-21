from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    completed = forms.BooleanField(required=False)
