from django import forms

from .models import DirectMessages

class ComposeForm(forms.ModelForm):
	class Meta:
		model = DirectMessages
		fields = ('receiver', 'subject', 'body')
		widgets = { 
			'body': forms.Textarea(attrs={'cols':80, 'rows':20}),
			}