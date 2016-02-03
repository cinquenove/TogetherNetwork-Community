# -*- coding=utf-8 -*-
from django.forms import ModelForm
from .models import Activity
from .models import Comment

class ActivityForm(ModelForm):
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

            "attendees_limit",
            #"attendees",
            "price"
        ]

        labels = {
            "title": "Title",
            "description": "Description",
            "activity_type": "Activity ype",

            "time": "Time",
            "location": "Where is the activity taking place?",
            "photo": "Cover image",

            "attendees_limit:": "Attendees Limit",
            
            "price": "Price",
        }
        help_texts = {
            'price': 'Se le modalità di pagamento sono disponibili nella descrizione, in questo campo scrivi \"-1\" ',
            'location': 'Se l\'attività non ha luogo nelle case, specificare l\'indirizzo nella descrizione',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            #"owner",
            "content"
            #"pub_date",
        ]