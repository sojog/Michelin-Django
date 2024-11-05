from django import forms

CHOICES = [
     (i, f'{i} item{'s' if i > 1 else '' }') for i in range(1, 11)
]

class ProductToCartForm(forms.Form):
    # quantity = forms.IntegerField(min_value=1, max_value=10)
     quantity =  forms.TypedChoiceField(choices=CHOICES)

class EmptyCartForm(forms.Form):
    pass