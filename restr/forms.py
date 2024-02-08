from django import forms
from .models import Review,Reservation
class SearchForm(forms.Form):
    search = forms.CharField(max_length=256)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'text', 'rating','restaurant']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'restaurant': forms.Select(attrs={'class': 'form-control'})
        }
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'time', 'restaurant','desired_table']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.DateTimeInput(attrs={'class': 'form-control','placeholder': ' ГГГГ-ММ-ДД ЧЧ:ММ'}),
            'restaurant': forms.Select(attrs={'class': 'form-control'}),
            'desired_table': forms.TextInput(attrs={'class': 'form-control'})
        }


