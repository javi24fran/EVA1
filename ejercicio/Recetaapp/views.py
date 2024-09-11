from django.shortcuts import render


def interfaz1(request):
    return render(request, 'templatesapp/index.html')

def interfaz2(request):
    return render(request, 'templatesapp/interfaz2.html')
    
    #def index(reuquest):
    #data= {
        #'Tarta de Manzana':'descripcion',
        #'Paella': 'descripcon2', data,}
   


# Create your views here.
