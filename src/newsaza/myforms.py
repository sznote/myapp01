from django import forms
from .models import SignUP

'''
#class SignUP(forms.Form):

    your_name = forms.CharField(label='username', max_length=100,help_text="Enter (a-zA-Z)")
    your_surname = forms.CharField(label='surname', max_length=100,help_text="Enter (a-zA-Z)")
    your_email = forms.EmailField(label='email',max_length=100)
    your_tel = forms.DecimalField(label='Tel', max_digits=12)
    #submit = forms.ChoiceField(label='hello',choices=count)ContactForm
    #mment = forms.CharField(widget=forms.Textarea)
    #test01 = forms.TextInput(attrs={'size': 10, 'title': 'hlloodf',})
    male = forms.BooleanField(required=True,initial='male')
    female = forms.BooleanField(required=False,initial='female',)

'''


class ContactForm (forms.Form):

    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUP
        fields = ['email', 'fullname', 'zipcode']
    count = (
        ('a','1'),
        ('b','2'),
        ('c','3'),
        ('d','4'),
    )

    def clean_mail(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_name(self):
        fullname = self.cleaned_data.get('fullname')
        return fullname

    def clean_zipcode(self):
        zipcode = self.cleaned_data.get('zipcode')
        return zipcode


class SazaForm(forms.Form):

    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

