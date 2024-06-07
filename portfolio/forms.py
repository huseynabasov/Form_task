from django import forms 
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person  
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})