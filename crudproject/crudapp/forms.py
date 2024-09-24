from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

        labels = {
            'oid': 'Order ID',
            'fname' : 'Products  Name',
            'lname' : 'Buyer Name.' ,
            'price' : 'Price' ,
            'mail' : 'Total',
            'addr' : 'Address' ,
        }

        widgets  ={
            'oid' : forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
            'fname' : forms.TextInput(attrs={'placeholder': 'eg.productt'}),
            'lname' : forms.TextInput(attrs={'placeholder': 'eg. name'}),
            'price' : forms.NumberInput(attrs={'placeholder': 'eg. 10000'}),
            'mail' : forms.NumberInput(attrs={'placeholder': 'eg. 10000'}),
            'addr' : forms.Textarea(attrs={'placeholder': 'eg. IN'}),
        }