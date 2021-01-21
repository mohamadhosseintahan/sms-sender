from django.urls import path
from .views import MessageList , MessageCreate , MessageDetail , MessageDelete
urlpatterns = [
    path('create/' , MessageCreate.as_view() , name = 'create'),
    path('<int:pk>/detail/' , MessageDetail.as_view() , name = 'detail'),
    path('<int:pk>/delete/' , MessageDelete.as_view() , name = 'delete'),
    path('' , MessageList.as_view() , name = 'list'),
]
