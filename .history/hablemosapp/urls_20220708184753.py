from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('debate/list', DebateList.as_view(), name="debate_list"),
    path('debate/<pk>', DebateDetail.as_view(), name="debate_detail"),
    path('debate/nuevo', DebateCreate.as_view(), name="debate_create"),
    path('debate/editar/<pk>', DebateUpdate.as_view(), name="debate_update"),
    path('debate/eliminar/<pk>', DebateDelete.as_view(), name="profe_delete"),
]