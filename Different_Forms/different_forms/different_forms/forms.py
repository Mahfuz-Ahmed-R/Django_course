from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    value = forms.DecimalField()
    email_address = forms.EmailField( 
    required = False,
)
    message = forms.CharField(
	max_length = 10,
)
    email_address = forms.EmailField( 
    label="Please enter your email address",
)
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput())
    