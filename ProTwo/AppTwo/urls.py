from django.urls import path
from AppTwo import views

urlpatterns = [
    path(r'',views.help,name='help'),
]