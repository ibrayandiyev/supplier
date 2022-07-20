from django import forms
from .models import User, Stock, Contact, Client, Command


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'picture', 'email', 'telephone')
        widgets = {
            'picture': forms.FileInput(attrs={'class':'custom-file-input','onchange':'readURL(this);'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', }),
            'last_name': forms.TextInput(attrs={'class':'form-control', }),
            'email': forms.TextInput(attrs={'class':'form-control', 'required': True, 'type':'email'}),
            'telephone': forms.TextInput(attrs={'class':'form-control', }),
            'username': forms.TextInput(attrs={'class':'form-control', }),
        }

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('name', 'reference', 'quantity', 'picture', 'category', 'user', 'minium', 'b_group', 'pdf', 'location', 'width', 'height', 'depth', 'weight')



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'picture', 'address', 'country', 'notes', 'telephone', 'mobile', 'email', 'web', 'products', 'pdf', 'parent', 'user', 'nif')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'picture', 'country', 'notes', 'telephone', 'mobile', 'email', 'web', 'products', 'pdf', 'parent', 'user', 'b_client', 'nif')

class CommandForm(forms.ModelForm):
    class Meta:
        model = Command
        fields = ('name', 'date', 'group', 'quantity', 'worker', 'user')