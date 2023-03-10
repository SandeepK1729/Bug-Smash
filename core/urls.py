from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('organizers', views.organizers, name = 'organizers'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register, name = 'register'),

    path('<str:model_name>s', views.general_table_view, name = 'table-view'),
    path('<str:model_name>/add', views.model_add, name = "modelAdd"),
    
    path('participants/verify', views.participantsVerification, name = 'participantVerification'),

    path('test/<str:test_name>', views.participateInTest, name = "participate"),
    path('test/<str:test_name>/results', views.test_results, name = "test_results"),
]