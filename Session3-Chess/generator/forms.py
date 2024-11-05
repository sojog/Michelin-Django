from django import forms


class PasswordGeneratorForm(forms.Form):
    password_size = forms.IntegerField(max_value=15, min_value=2, required=True, initial=2, label="Password length")

    has_uppercase = forms.BooleanField(label="Include uppercase?", required=False)

    has_numbers = forms.BooleanField(label="Include numbers?", required=False)

    has_special_ch = forms.BooleanField(label="Include special characters?", required=False)
