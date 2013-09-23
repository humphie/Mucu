from django import forms

class ContactsForm(forms.Form):
	name    = forms.CharField(max_length = 30)
	e_mail  = forms.EmailField(max_length = 45)
	subject = forms.CharField(max_length = 40)
	message = forms.CharField(max_length = 500, widget=forms.Textarea)
