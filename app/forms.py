from django import forms

class SchoolForm(forms.Form):
    Sname=forms.CharField(max_length=100)
    Sage=forms.IntegerField(min_value=5)
    Semail=forms.EmailField()
    Surl=forms.URLField()
    Spassword=forms.CharField(widget=forms.PasswordInput)
    Saddress=forms.CharField(widget=forms.Textarea(attrs={'cols':10, 'rows':5}))
