from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.views.generic.base import TemplateView


urlpatterns = [
    # path('', views.login, name='login'),
    # path('login', TemplateView.as_view(template_name='home.html'),name='home'),
    path('',views.inicio , name = 'inicio'),
    path('empleados', views.empleados, name='empleados'),
    path('empleados/crear', views.crear_empleado, name='crear'),
    path('empleados/editar', views.editar_empleado, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name= 'eliminar'),
    path('empleados/editar/<int:id>', views.editar_empleado, name='editar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)