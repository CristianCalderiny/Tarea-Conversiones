from django import forms
import re

class BinarioForm(forms.Form):
    numero_binario = forms.CharField(
        label='Número Binario',
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese un número binario (ej: 1010)',
            'pattern': '[01]+',
            'title': 'Solo se permiten los dígitos 0 y 1'
        })
    )
    
    def clean_numero_binario(self):
        numero = self.cleaned_data['numero_binario']
        
        # Validar que solo contenga 0s y 1s
        if not re.match(r'^[01]+$', numero):
            raise forms.ValidationError(
                'El número ingresado no es un binario válido. '
                'Solo se permiten los dígitos 0 y 1.'
            )
        
        return numero