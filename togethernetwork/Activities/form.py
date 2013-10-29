from django.forms import ModelForm
from .models import Activity

class ProfileForm(ModelForm):
    class Meta:
        model = Activity
        fields = [
            #"owner",
            "title",
            "description",
            "activity_type",

            "time",
            "location",
            "photo",

            "attendee_limit",
            #"attendee",
            "price",
        ]