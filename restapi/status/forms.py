from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'description',
            'cost'
        ]

    def clean_description(self, *args, **kwargs):
        description = self.cleaned_data.get('description')
        if len(description) > 240:
            raise forms.ValidationError("Description is too long")
        return description

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        description = data.get('description', None)
        cost = data.get('cost', None)
        if description == "":
            description = None
        if description is None and cost is None:
            raise forms.ValidationError("Description or cost is required.")
        return super().clean(*args, **kwargs)