from django import forms 

class create_list(forms.Form):
	name = forms.CharField(label = "name", max_length = 200)
	Verify = forms.BooleanField(required = False)
