from django import forms
from app.models import *

class Topicform(forms.Form):
    topic_name=forms.CharField()

class Webpageform(forms.Form):
    TL=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]

    topic_name=forms.ChoiceField(choices=TL)
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()

class Accessrecordform(forms.Form):
    AL=[[wo.pk,wo.name] for wo in Webpage.objects.all()]

    name=forms.ChoiceField(choices=AL)
    date=forms.DateTimeField()
    author=forms.CharField()