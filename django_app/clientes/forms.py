from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'#['first_name', 'last_name' ,'age', 'salary', 'bio','fale_mais','photo']
