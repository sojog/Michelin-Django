from django import forms
from django.core.exceptions import ValidationError

def skip_9_validator(value):
    if not (value in range(4, 9)) or (value in range(10, 13)):
        raise ValidationError("The value should be between 4 and 8 or 4 and 12")

class SizeForm(forms.Form):
    size = forms.IntegerField(min_value=4, max_value=12, validators=[skip_9_validator])


