from django import forms


class SignUP(forms.Form):

    count = (
        ('a','1'),
        ('b','2'),
        ('c','3'),
        ('d','4'),
    )
    your_name = forms.CharField(label='username', max_length=100,initial='',help_text="Enter (a-zA-Z)")
    your_surname = forms.CharField(label='surname', max_length=100,help_text="Enter (a-zA-Z)")
    your_email = forms.EmailField(label='email',max_length=100)
    your_tel = forms.DecimalField(label='Tel', max_digits=12)
    submit = forms.ChoiceField(label='hello',choices=count)
    #mment = forms.CharField(widget=forms.Textarea)
    #test01 = forms.TextInput(attrs={'size': 10, 'title': 'hlloodf',})
    male = forms.BooleanField(required=True,initial='male')
    female = forms.BooleanField(required=False,initial='female',)


