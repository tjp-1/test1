from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view),
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('show/', views.show_view),
    path('info/', views.info_view),
    path('infoShow/',views.showInfo_view),
    path('getstu/',views.getStu_view)
]
