from django.forms import ModelForm
from vacations.models import Location

# Create the form class.
class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
