from django.shortcuts import render
from .forms import BinarioForm

def convertir_binario(request):
    resultado = None
    error = None
    
    if request.method == 'POST':
        form = BinarioForm(request.POST)
        if form.is_valid():
            # Obtener el número binario del formulario
            binario = form.cleaned_data['numero_binario']
            
            try:
                # Realizar las conversiones
                decimal = int(binario, 2)
                octal = oct(decimal)[2:]  # [2:] para quitar el prefijo '0o'
                hexadecimal = hex(decimal)[2:].upper()  # [2:] para quitar '0x'
                
                # Preparar los resultados
                resultado = {
                    'binario': binario,
                    'decimal': decimal,
                    'octal': octal,
                    'hexadecimal': hexadecimal
                }
            except ValueError:
                error = 'Error al procesar el número binario.'
        else:
            error = 'Por favor, ingrese un número binario válido.'
    else:
        form = BinarioForm()
    
    context = {
        'form': form,
        'resultado': resultado,
        'error': error
    }
    
    return render(request, 'conversor/index.html', context)