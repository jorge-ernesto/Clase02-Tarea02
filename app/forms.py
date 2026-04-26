from django import forms
from .models import Alumno

# El formulario hereda las validaciones definidas en el modelo.
class AlumnoForm(forms.ModelForm):
    # Aplicar cambios en inputs del formulario (Otra forma)
    # fecha = forms.DateField(
    #     widget=forms.DateInput(attrs={'type': 'date'})  # widget=forms.SelectDateWidget()
    # )

    class Meta:
        model = Alumno
        fields = '__all__'
        # fields = ['codigo', 'nombre', 'apellidos', 'fecha_nacimiento', 'edad', 'email', 'telefono', 'estado']  # Otra forma
        # Aplicar cambios en inputs del formulario
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'edad': forms.NumberInput(attrs={'disabled': 'disabled', 'placeholder': 'Se calculara automaticamente'})
        }
