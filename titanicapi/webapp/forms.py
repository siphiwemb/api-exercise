
from django import forms
from .models import Titanic

class TitanicForm(forms.ModelForm):
    class Meta:
        model = Titanic
        fields = ['survived', 'name', 'sex', 'age', 'fare']

    passengerClass = forms.IntegerField()
    siblingsOrSpousesAboard = forms.IntegerField()
    parentsOrChildrenAboard = forms.IntegerField()
    uuid = forms.CharField(max_length=120, required=False)

    def save(self, commit=True):
        data = self.cleaned_data
        uuid = data['uuid']

        defaults = {
            'survived': data['survived'],
            'passenger_class': data['passengerClass'],
            'name': data['name'],
            'sex': data['sex'],
            'age': data['age'],
            'siblings_spousesaboard': data['siblingsOrSpousesAboard'],
            'parents_childrenaboard': data['parentsOrChildrenAboard'],
            'fare': data['fare']
        }

        if uuid == "":
            save_obj = Titanic(**defaults)
            save_obj.save()
            return save_obj
        else:
            Titanic.objects.filter(uuid=uuid).update(**defaults)
            updated_obj = Titanic.objects.get(uuid=uuid)
            return updated_obj

