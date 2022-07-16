from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="" ,widget=forms.TextInput(attrs={'class': 'form-control mt-1 mb-1', 'placeholder': 'Enter your Email'}))
    
    first_name = forms.CharField(label="", max_length=30,  widget=forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Enter your First Name'}))
    last_name = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Enter your Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def  __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

       

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Username'
        self.fields['username'].label=''
        self.fields['username'].help_text = '<span class="form-text text-muted " style="margin-top:-20px;"> <small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
       

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Your Password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text = '<small class=""><ul class="form-text text-muted " style="list-style:none; margin-top:-20px;"><li style="list-style:none; color:red">Your password cant be too similar to your other personal information.</li><li style="list-style:none; color:red">Your password must contain at least 8 characters.</li><li style="list-style:none; color:red"> Your password cant be a commonly used password.</li><li style="list-style:none; color:red"> Your password cant be entirely numeric.</li></ul></small>'

        self.fields['password2'].widget.attrs['class'] = 'form-control '
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Your Password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text = '<span class="form-text text-muted" style="list-style:none; margin-top: -20px"> <small>Enter the same password as before, for verification.</small></span>'