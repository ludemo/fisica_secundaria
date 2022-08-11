
from django.contrib import admin
from django.urls import path, include
from noLineales.views import home_view, mabiertos
from calculadora.views import Index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view() , name="home"),
    path('admin/', admin.site.urls),
    path('Ecuaciones-no-lineales/', include('noLineales.urls')),
    path('Ecuaciones-algebraicas/', include('algebraicas.urls')),
    path('Ajuste-interpolacion/', include('curvas.urls')),
    path('movimiento_en_una_dimension/', include('Movimento_una_dimension.urls')),
    path('analisis_vectorial/', include('Vectores.urls')),
    path('estatica/', include('Estatica.urls')),
    path('dinamica/', include('Dinamica.urls')),
    path('temperatura/', include('Temperatura.urls')),
    path('electroestatica/', include('Electroestatica.urls')),
    path('electrodinamica/', include('Electrodinamica.urls')),
    path('teoria_relatividad/', include('Teorida_Relatividad.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
