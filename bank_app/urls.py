from django.urls import path
from . import views

urlpatterns = [
    path('branches/autocomplete/', views.BranchAutoComplete),
    path('branches', views.AutoComplete),
]
