from django.urls import path
from . import views
app_name = 'adddev'
urlpatterns = [
    path('data/', views.DevloperData, name='DevloperData'),
    path('edit/<int:id>', views.edit_view, name='DevloperData'),
]
