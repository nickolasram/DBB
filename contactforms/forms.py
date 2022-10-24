from django import forms
from .tasks import send_email_task, send_own_email_task

class Contact_Form(forms.Form):
    fname = forms.CharField(
        label='First name:', min_length=4, max_length=50, required=True,
        widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder': 'required',
                                      'id': 'form-fname', 'name': 'fname'})
    )
    lname = forms.CharField(
        label='Last name:', min_length=4, max_length=50, required=True,
        widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder': 'required',
                                      'id': 'form-lname', 'name': 'lname'})
    )
    company = forms.CharField(
        label='Company:', min_length=4, max_length=50, required=False,
        widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder': 'optional',
                                      'id': 'form-company', 'name': 'company'})
    )
    email = forms.EmailField(
        label='Email:', min_length=4, max_length=50, required=True,
        widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder': 'required',
                                      'id': 'form-email', 'name': 'email'})
    )
    body = forms.CharField(
        label='Message body:', min_length=4, required=True,
        widget=forms.Textarea(attrs={'class': 'textareainput', 'placeholder': 'required',
                                     'id': 'form-body', 'name': 'body', 'rows': '15', 'cols': '30'})
    )

    def send_email(self):
        send_email_task.delay( self.cleaned_data['fname'],self.cleaned_data['email'],
                               self.cleaned_data['body'],self.cleaned_data['lname'],self.cleaned_data['company'])
        send_own_email_task.delay(self.cleaned_data['fname'], self.cleaned_data['email'],
                              self.cleaned_data['body'], self.cleaned_data['lname'], self.cleaned_data['company'])


class Bug_Form(forms.Form):
    fname = forms.CharField(
        label='First name:', min_length=4, max_length=50, required=True,
        widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder': 'required',
                                      'id': 'form-fname', 'name': 'fname'})
    )
    lname = forms.CharField(
        label='Last name:', min_length=4, max_length=50, required=False,
        widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder': 'optional',
                                      'id': 'form-lname', 'name': 'lname'})
    )
    email = forms.EmailField(
        label='Email:', min_length=4, max_length=50, required=True,
        widget=forms.TextInput(attrs={'class': 'textinput', 'placeholder': 'required',
                                      'id': 'form-email', 'name': 'email'})
    )
    body = forms.CharField(
        label='Message body:', min_length=4, required=True,
        widget=forms.Textarea(attrs={'class': 'textareainput', 'placeholder': 'required',
                                     'id': 'form-body', 'name': 'body', 'rows': '15', 'cols': '30'})
    )

    def send_email(self):
        send_email_task.delay(self.cleaned_data['fname'], self.cleaned_data['email'],
                              self.cleaned_data['body'], self.cleaned_data['lname'], None)
        send_own_email_task.delay(self.cleaned_data['fname'], self.cleaned_data['email'],
                                  self.cleaned_data['body'], self.cleaned_data['lname'], None)