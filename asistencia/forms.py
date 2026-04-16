from django import forms
from .models import Asistencia


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = [
            'nombre_completo',
            'documento',
            'correo',
            'fecha',
            'hora_ingreso',
            'hora_salida',
            'presente',
            'observaciones',
        ]
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'maxlength': 150, 'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_ingreso': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hora_salida': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'presente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_nombre_completo(self):
        nombre = self.cleaned_data.get('nombre_completo', '')
        return nombre.strip()
