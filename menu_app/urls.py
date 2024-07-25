from django.urls import path
from .views import MenuView,StartMenuView

urlpatterns = [
    path('<path:menu_url>/', MenuView.as_view(), name='detail_menu'),  
    path('', StartMenuView.as_view(), name='start_menu')
]