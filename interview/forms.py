from django import forms

class contactForm(forms.Form):
	name = forms.CharField(required=True, max_length=100, help_text='100 characters max')
	email = forms.EmailField(required=False)
	question_asked_in_company = forms.CharField(required=True, max_length=200)
	question_title = forms.CharField(required=True, max_length = 100)
	description_of_the_Question = forms.CharField(required = True,  widget=forms.Textarea)
	input = forms.CharField(required=True, max_length=200)
	output = forms.CharField(required=True, max_length=200)