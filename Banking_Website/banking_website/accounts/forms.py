from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserBankAccount, UserAddress
from .constants import ACCOUNT_TYPE, GENDER_TYPE


class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    account_type = forms.ChoiceField( choices=ACCOUNT_TYPE)
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'birth_date', 'email', 'account_type', 'gender', 'street_address', 'postal_code', 'city', 'country', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit==True:
            user.save()
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            street_address = self.cleaned_data.get('street_address')
            postal_code = self.cleaned_data.get('postal_code')
            city = self.cleaned_data.get('city')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')

            UserBankAccount.objects.create(
                user=user,
                account_type=account_type,
                gender = gender,
                birth_date= birth_date,
                account_no = 1000 + user.id
            )
            UserAddress.objects.create(
                user=user,
                street_address=street_address,
                postal_code=postal_code,
                city=city,
                country=country
            )
        return user
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            
            for field in self.fields:
                self.fields[field].widget.attrs.update({
                     'class': (
                        'appearance-none block w-full bg-gray-200 '
                        'text-gray-700 border border-gray-200 rounded '
                        'py-3 px-4 leading-tight focus:outline-none '
                        'focus:bg-white focus:border-gray-500'                        
                     )
                     
                    })
                
class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    account_type = forms.ChoiceField( choices=ACCOUNT_TYPE)
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                    'class': (
                        'appearance-none block w-full bg-gray-200 '
                        'text-gray-700 border border-gray-200 rounded '
                        'py-3 px-4 leading-tight focus:outline-none '
                        'focus:bg-white focus:border-gray-500'                        
                     )
                    })
            if self.instance:
                try:
                    user_account = self.instance.account
                    user_address = self.instance.address
                except UserBankAccount.DoesNotExist:
                    user_account = None
                    user_account = None
            
            if user_account:
                self.fields['account_type'].initial = user_account.account_type
                self.fields['gender'].initial = user_account.gender
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['street_address'].initial = user_account.street_address
                self.fields['city'].initial = user_account.city
                self.fields['postal_code'].initial = user_account.postal_code
                self.fields['country'].initial = user_account.country

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit==True:
            user.save()
            
            user_account, created = UserBankAccount.objects.get_or_create(user=user)
            user_address, created = UserAddress.objects.get_or_create(user=user)

            user_account.account_type = self.cleaned_data.get('account_type')
            user_account.gender = self.cleaned_data.get('gender')
            user_account.birth_date = self.cleaned_data.get('birth_date')
            
            user_address.street_address = self.cleaned_data.get('street_address')
            user_address.postal_code = self.cleaned_data.get('postal_code')
            user_address.city = self.cleaned_data.get('city')
            user_address.country = self.cleaned_data.get('country')

        return user
