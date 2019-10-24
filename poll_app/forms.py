from django.forms import ModelForm
from . import models


class VotoForm(ModelForm):

    class Meta:
        model = models.Poll_questions
        fields = '__all__'
