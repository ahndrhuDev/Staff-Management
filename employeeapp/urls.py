from django.urls import path
from employeeapp.views import(
    CreateView,
    EmployeeListViewSet
)

urlpatterns = [
    path('', CreateView.as_view(), name='create'),
    path('read/', EmployeeListViewSet.as_view(), name='read')
]