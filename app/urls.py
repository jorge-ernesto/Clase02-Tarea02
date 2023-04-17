from django.urls import path
from . import views

urlpatterns = [
    path(''                , views.alumno_form  , name='alumno_insert'),  # get y post req. para  insert
    path('<int:id>/'       , views.alumno_form  , name='alumno_update'),  # get y post req. para update
    path('delete/<int:id>/', views.alumno_delete, name='alumno_delete'),  # para eliminar
    path('list/'           , views.alumno_list  , name='alumno_list')     # get req. para recuparar y listar todos los registros
]
