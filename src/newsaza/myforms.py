from django import forms


class SignUP(forms.Form):

    count = (
        ('a','1'),
        ('b','2'),
        ('c','3'),
        ('d','4'),
    )
    your_name = forms.CharField(label='username', max_length=100,initial='sahai')
    your_surname = forms.CharField(label='surname', max_length=100)
    your_email = forms.EmailField(label='email',max_length=100)
    your_tel = forms.DecimalField(label='Tel', max_digits=12)
    submit = forms.ChoiceField(label='hello',choices=count)
    comment = forms.CharField(widget=forms.Textarea)
    meme = forms.TextInput(attrs={'size': 10, 'title': 'hlloodf',})

